from abc import ABC, abstractmethod
from keyboard import add_hotkey  # type: ignore
from keyboard import wait as keyboard_wait  # type: ignore
from keyboard import remove_hotkey  # type: ignore
from random import choice
from json import load as json_load
from json import dumps as json_dumps

win_cond_ruleset_dict = {'rock': {'scissors': 'crushes', 'lizard': 'crushes'},
                         'scissors': {'paper': 'cuts', 'lizard': 'decapitates'},
                         'paper': {'rock': 'covers', 'spock': 'disproves'},
                         'lizard': {'paper': 'eats', 'spock': 'poisons'},
                         'spock': {'rock': 'vaporizes', 'scissors': 'smashes'}
                         }


class FigureComparisonResult:
    """
    Instance contain one possible outcome for figures comparison
    Support inversion of resolution by using minus win -> lose, lose -> win, draw -> draw
    """
    resolution: str = ''
    win_word: str = ''

    def __init__(self, resolution: str, win_word: str = ''):
        self.resolution = resolution
        self.win_word = win_word

    def __str__(self):
        return str(self.resolution)

    def __neg__(self):
        if self.resolution == 'win':
            return 'lose'
        elif self.resolution == 'lose':
            return 'win'
        elif self.resolution == 'draw':
            return self.resolution


class FigureMove:
    """
    Creates all possible combinations of this move and all the other moves.
    Creates as many attributes named as there are possible moves. One attribute for other move this one could be combined.
    Creates FigureComparisonResult objects for each combination of moves, refers to te object in oher move attribute

    FigureComparisonResult instance could be accessed in two ways:
    first_figure_move_instance.second_move_name -> comparison_result_instance
    or
    first_figure_move_instance + second_figure_move_instance -> comparison_result_instance
    """
    move_name = ''

    def __init__(self, first_move: str, init_rules_set: dict[str, dict[str, str]]):
        """
        Assigns first_move as an internal name of the figure
        Analises init_rules_set, creates instance of FigureComparisonResult for each possible combination of this figure
        with each possible winning figure in init_rules_set. Creates all: winning, loosing, drawing outcomes
        (init_rules_set ought to contain only winning combination)
        Checks for conflicting winning combinations in init_rules_set
        Args:
            first_move: this move name, all the other moves will be compared to this one in the instance
            init_rules_set: initial rules set. Logic from it shall be applied to creation of figures comparison outcomes
        """
        self.move_name = first_move

        for other_move in init_rules_set.keys():
            if other_move in init_rules_set[first_move]:
                if first_move in init_rules_set[other_move]:
                    raise ValueError(f'Error: There is a conflict in ruleset. Combination of {first_move} and \
                                    {other_move} has conflicting winning conditions')
                else:
                    if init_rules_set[first_move][other_move]:
                        win_word = init_rules_set[first_move][other_move]
                    else:
                        win_word = 'overcomes'
                    self.__dict__[other_move] = FigureComparisonResult(resolution='win', win_word=win_word)

            else:
                if first_move in init_rules_set[other_move]:
                    self.__dict__[other_move] = FigureComparisonResult(resolution='lose', win_word='loses to')
                else:
                    self.__dict__[other_move] = FigureComparisonResult(resolution='draw')

    def __str__(self):
        return self.move_name.capitalize()

    def __add__(self, other):
        if not isinstance(other, FigureMove):
            raise TypeError(f'Error: only two objects of {FigureMove} class')
        return self.__dict__[other.move_name]


class GameRulesSet:
    """
    Contains OOP representation of all possible wiining, loosing and drawing combinations
    Creates a tree of FigureMove objects basing on the logic of full_rules_set dict
    Raises error if full_rules_set is empty, or contains moves without any possible winning combination
    """
    init_rules_set: dict = {}
    figure_moves_list: list[type] = []

    def __init__(self, full_rules_set: dict[str, dict[str, str]]):
        self.init_rule_set = full_rules_set
        if not full_rules_set:
            raise ValueError('Error: rules_set must not be empty')
        for first_move in self.init_rule_set.keys():
            for other_move in self.init_rule_set[first_move].keys():
                if other_move not in self.init_rule_set.keys():
                    raise ValueError(f'Error: rule set contains loosing move {other_move} which does '
                                     f'not exist in winning moves of a ruleset')
            self.__dict__[first_move] = FigureMove(first_move=first_move, init_rules_set=self.init_rule_set)
            self.figure_moves_list.append(self.__dict__[first_move])

    def __str__(self):
        return str(self.init_rule_set)


class GamesSettingsSingleton:
    """
    Contains and stores all the current game settings. Works as a storage of references to other objects.
    Works as an intermediary between objects. Other objects know only about this one, and this one provides references
    to all the others.
    game_rule_set instance, screen_views, human_player, ai_player are expected to assign references to their instances
        during initialization of those instances. When done GamesSettingsSingleton provides references
        to game_rule_set instance, screen_views, human_player, ai_player instances to other objects
    """
    _instance_for_singleton = None
    human_player: object
    human_player_name: str = 'xarvioto'
    ai_player: object
    ai_player_name: str = 'MR. BOT'
    choose_next_button = 'down'
    choose_previous_button = 'up'
    confirm_selection_button = 'enter'
    win_cond_ruleset = win_cond_ruleset_dict
    game_rule_set: object = None
    screen_views: object = None

    statistics_file_name = 'statistics.txt'
    # settings_file_name = 'settings.txt'
    rules_set_file_name = 'rules_set.txt'

    def __new__(cls):
        if not cls._instance_for_singleton:
            cls._instance_for_singleton = super().__new__(cls)
        return cls._instance_for_singleton

    def load_rules_set_from_file(self, rules_set_file_name):
        try:
            with open(rules_set_file_name, 'rt') as file1:
                self.game_rule_set = GameRulesSet(json_load(file1))
        except FileNotFoundError:
            self.game_rule_set = GameRulesSet(self.win_cond_ruleset)
            with open(rules_set_file_name, 'wt') as file2:
                rules_to_write = json_dumps(win_cond_ruleset_dict)
                file2.write(rules_to_write)
            print(f'Error: {rules_set_file_name} file was not found. DEFAULT rules were applied and '
                  f'{rules_set_file_name} file was created with default rules')

    def __init__(self):
        if not self.game_rule_set:
            self.load_rules_set_from_file(self.rules_set_file_name)


class PlayerABC(ABC):
    player_type = ''
    screen_views: object

    @abstractmethod
    def __init__(self, game_settings_object: GamesSettingsSingleton):
        pass

    @abstractmethod
    def generate_figure(self):
        pass

    @abstractmethod
    def ask_input_name(self):
        pass


class GameScreens:
    """
    Provides methods to represent the game progress to user. Print representations and stuff
    Grabs all the quite a few piece of info about the game through access to GamesSettingsSingleton
    (control buttons, info about current player names)
    """
    game_settings: GamesSettingsSingleton

    def __init__(self, game_settings_object: GamesSettingsSingleton = GamesSettingsSingleton()):
        self.game_settings = game_settings_object
        game_settings_object.screen_views = self

    def selection_menu_view(self, menu_title: str, menu_options: list[str | object]):
        """
        Shows the list of options, expects user to choose one from the list by using keys defined for UP, DOWN and ENTER
        Args:
            menu_title: The title shown while selecting options
            menu_options (tuple, list): tuple of possible options to choose and later return

        Returns:
            str: one of elements from the menu_options
        """
        current_selection = 1
        list_length = len(menu_options)
        enum_tuple = list(enumerate(menu_options, start=1))

        up_button = self.game_settings.choose_previous_button
        down_button = self.game_settings.choose_next_button
        confirm_button = self.game_settings.confirm_selection_button

        def show_the_options_with_selection(prompt_to_show, enum_tuple_of_options):
            nonlocal current_selection
            print('\n')
            print(prompt_to_show)
            print(f'Please use -> {up_button.upper()} <-, -> {down_button.upper()} <- to go up and down, '
                  f'and -> {confirm_button.upper()} <- for confirmation of your choice')
            for num, element in enum_tuple_of_options:
                print(f'{"-->" if current_selection == num else "   "} '
                      f'{num}. {str(element)} '
                      f'{"<--" if current_selection == num else "   "}')

        def move_one_menu_item_up():
            nonlocal current_selection
            if current_selection == 1:
                return
            current_selection -= 1
            show_the_options_with_selection(menu_title, enum_tuple)

        def move_one_menu_item_down():
            nonlocal current_selection
            if current_selection == list_length:
                return
            current_selection += 1
            show_the_options_with_selection(menu_title, enum_tuple)

        show_the_options_with_selection(menu_title, enum_tuple)
        add_hotkey(up_button, move_one_menu_item_up)
        add_hotkey(down_button, move_one_menu_item_down)

        keyboard_wait(confirm_button)

        remove_hotkey(up_button)
        remove_hotkey(down_button)

        return enum_tuple[current_selection - 1][1]

    @staticmethod
    def moves_comparison_battle_string(figure, player, mode):
        """
        Generates somewhat random battlelog entries to show Players' deep engagement into battle:

        Args:
            figure (FigureMove): FigureMove object
            player (PlayerABC): Player object
            mode (str): there are two modes 'first_strike' and 'riposte'
        Returns:
            str: stylized message of player showing particular figure
        """
        fig = str(figure).capitalize()
        name = player.player_name

        frases_dict = {'starters1': ['So', 'Initially', 'At first', 'At the very beginning'],
                       'midds12': [f'makes {fig} move', f'strikes with {fig}',
                                   f'shows {fig}'],
                       'starters2': ['But suddenly', 'But', 'After that', 'At the end of the day', 'While'],
                       'enders2': ['right off the bat', 'at the same time', 'like there is no tomorrow']
                       }
        if mode == 'first_strike':
            print(f'First strike: {choice(frases_dict["starters1"])}, {name} {choice(frases_dict["midds12"])}')
        elif mode == 'riposte':
            print(f'Riposte: {choice(frases_dict["starters2"])}, {name} {choice(frases_dict["midds12"])} '
                  f'{choice(frases_dict["enders2"])}')

    def resolution_string(self, figure_1: FigureMove, figure_2: FigureMove,
                          figure_comparison_result_object: FigureComparisonResult):

        if figure_comparison_result_object.resolution == 'draw':
            print(f'{figure_1} vs {figure_2}')
            print('Round result: a Draw')

        elif figure_comparison_result_object.resolution == 'win':
            print(f'{figure_1} {figure_comparison_result_object.win_word} {figure_2}')
            print(f'Round result: {self.game_settings.human_player_name} won')

        elif figure_comparison_result_object.resolution == 'lose':
            print(f'{figure_1} {figure_comparison_result_object.win_word} {figure_2}')
            print(f'Result: {self.game_settings.ai_player_name} won')
        else:
            raise Exception('Error. Round resolution failed for some strange reason')
            # log_file.write(f'Error. Round resolution failed for some strange reason')


class HumanPlayer(PlayerABC):
    """
    Contains Human player related stuff.
    Stores player name (gets from and sets to) in GamesSettingsSingleton
    Grabs access to GameScreens through GamesSettingsSingleton
    """
    def __init__(self, game_settings_object: GamesSettingsSingleton = GamesSettingsSingleton()):
        self.game_settings = game_settings_object
        self.screen_views = self.game_settings.screen_views
        self.player_type = 'Human'

        if not self.player_name:
            self.ask_input_name()

        game_settings_object.human_player = self

    @property
    def player_name(self):
        return self.game_settings.human_player_name

    @player_name.setter
    def player_name(self, value):
        self.game_settings.human_player_name = value

    def ask_input_name(self):
        enter_your_name_prompt = 'Hey Player, please enter your name:'
        self.player_name = input(enter_your_name_prompt).strip()

    @property
    def generate_figure(self):
        """
        Asks user to choose one of figure moves
        Returns:
            (FigureMove): Object of FigureMove class, that contains links to outcomes of comparison

        """
        selection_menu = self.screen_views.selection_menu_view
        player_move_result = selection_menu(menu_title=f'Hey {self.player_name}, please choose figure to play:',
                                            menu_options=self.game_settings.game_rule_set.figure_moves_list)

        return player_move_result


class AiPlayer(PlayerABC):
    """
    Contains AI player related stuff.
    """
    def __init__(self, game_settings_object: GamesSettingsSingleton = GamesSettingsSingleton()):
        self.game_settings = game_settings_object
        self.screen_views = self.game_settings.screen_views
        self.player_type = 'AI'

        if not self.game_settings.ai_player_name:
            self.ask_input_name()

        game_settings_object.ai_player = self

    @property
    def player_name(self):
        return self.game_settings.ai_player_name

    @player_name.setter
    def player_name(self, value):
        self.game_settings.ai_player_name = value

    def ask_input_name(self):
        enter_your_name_prompt = 'Hey Player, please enter name for AI:'
        self.player_name = input(enter_your_name_prompt).strip()

    @property
    def generate_figure(self):
        """
         Grabs a list of possible moves from Settings object.
         Returns random figure object from the list
         Returns:
             str: random element of list_of_options
         """
        ai_move_result = choice(self.game_settings.game_rule_set.figure_moves_list)
        return ai_move_result


class GameSession:
    """
    Controls current game session (which could consist of many game rounds).
    Updates statistics into a file if instance of class is run in context manager.
    """
    game_settings = None
    screen_views = None
    player_1_name: str = ''
    player_2_name: str = ''
    session_statistics_dict: dict = {}
    statistics_file_name: str = ""

    def __init__(self, game_settings_object: GamesSettingsSingleton = GamesSettingsSingleton()):

        self.game_settings = game_settings_object
        self.screen_views = self.game_settings.screen_views
        self.player_1 = self.game_settings.human_player
        self.player_2 = self.game_settings.ai_player
        self.player_1_name = self.game_settings.human_player_name
        self.player_2_name = self.game_settings.ai_player_name

        self.statistics_file_name = self.game_settings.statistics_file_name

        self.session_statistics_dict.update({self.player_1_name: {}})
        self.session_statistics_dict.update({self.player_2_name: {}})

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.update_statistics_in_file()
        return True

    def play_one_round(self):
        """
        Defines the winner between two figures according to ruleset:
        Accept two figures, checks if combination exists in ruleset, decides which figure is a winner
        prints intermediary resolution results.
        """
        figure_1 = self.player_1.generate_figure
        self.screen_views.moves_comparison_battle_string(figure=figure_1, player=self.player_1, mode='first_strike')
        figure_2 = self.player_2.generate_figure
        self.screen_views.moves_comparison_battle_string(figure=figure_2, player=self.player_2, mode='riposte')

        round_resolution_object = figure_1 + figure_2
        self.screen_views.resolution_string(figure_1, figure_2, round_resolution_object)

        self.accumulate_session_statistics(figure_1, figure_2, round_resolution_object)
        return 'Round ends'

    def accumulate_session_statistics(self, figure_1: FigureMove, figure_2: FigureMove, round_resolution_object):
        """
        Gets played figures objects as well as existent round resolution objects.
        Accumulates statistics of current game session by updating statistics dict at self
        Args:
            figure_1 (FigureMove): figure played by player 1
            figure_2 (FigureMove): figure played by player 2
            round_resolution_object (FigureComparisonResult): round resolution b

        """
        # player 1
        fig_1 = str(figure_1)
        fig_2 = str(figure_2)
        resol = round_resolution_object
        player_1_name = self.player_1_name
        player_2_name = self.player_2_name
        stat_dict = self.session_statistics_dict

        # player_1
        stat_dict[player_1_name].update({fig_1: stat_dict[player_1_name].get(fig_1, 0) + 1})
        stat_dict[player_1_name].update({str(resol): stat_dict[player_1_name].get(str(resol), 0) + 1})

        # player_2
        stat_dict[player_2_name].update({fig_2: stat_dict[player_2_name].get(fig_2, 0) + 1})
        stat_dict[player_2_name].update({str(-resol): stat_dict[player_2_name].get(str(-resol), 0) + 1})

    def play_game_session(self):
        """
        Provides an infinite loop of rounds and asking user for permition to proceed with another round.
        If user answers NO - loop breaks
        """
        while True:
            self.play_one_round()
            another_round_selection = self.screen_views.selection_menu_view(
                menu_title="Do you want to play another round?",
                menu_options=['Yes', 'No'])

            if another_round_selection == "No":
                print('Thank you for playing. Exiting now')
                break
            else:
                print('Another round then...')

    def update_statistics_in_file(self):
        """
        Reads previous statistics from txt files as json
        Adds statistics of the current game session (key by key, number by number)
        Writes updates statistics over the old file as json
        """
        try:
            with open(self.statistics_file_name, 'rt') as file:
                old_dict_from_file = json_load(file)
        except FileNotFoundError:
            old_dict_from_file = {}

        current_dict = self.session_statistics_dict
        upd_stat = old_dict_from_file
        if upd_stat:
            for name_key in set(upd_stat) | set(current_dict):
                if not upd_stat.get(name_key, 0):
                    upd_stat.update({name_key: {}})
                if not current_dict.get(name_key, 0):
                    current_dict.update({name_key: {}})

                for stat_item_key in set(upd_stat.get(name_key, {})) | set(current_dict.get(name_key, {})):

                    upd_value = upd_stat[name_key].get(stat_item_key, 0)
                    curr_value = current_dict[name_key].get(stat_item_key, 0)

                    upd_stat[name_key].update({stat_item_key: upd_value + curr_value})

        else:
            upd_stat = self.session_statistics_dict

        with open(self.statistics_file_name, 'wt') as file:
            json_to_save = json_dumps(upd_stat)
            file.write(json_to_save)
