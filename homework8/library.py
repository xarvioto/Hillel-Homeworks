from json import load as json_load
from json import dumps as json_dumps
from random import choice
from datetime import datetime
from keyboard import add_hotkey
from keyboard import wait as keyboard_wait
from keyboard import remove_hotkey


win_cond_ruleset_dict = {'Rock': {'Scissors': 'crushes',
                                  'Lizard': 'crushes'},
                         'Scissors': {'Paper': 'cuts',
                                      'Lizard': 'decapitates'},
                         'Paper': {'Rock': 'covers',
                                   'Spock': 'disproves'},
                         'Lizard': {'Paper': 'eats',
                                    'Spock': 'poisons'},
                         'Spock': {'Rock': 'vaporizes',
                                   'Scissors': 'smashes'}
                         }
"""
Contains all possible win condition with the structure:
{winner's figure : {loser's figure : the way victor's figure overcome loser's figure}} -> Rock crushed Scissors
"""


def get_player_figure_input(list_of_options):
    """
    Requests user's figure for the current round, validates and returns it:
    Displays all possible options to user before requesting, and assigns a number to it.
    Allows user input as either number of move, or full name of figure
    Shows informative Error instruction for every case of unsuccessful input validation

    Args:
        list_of_options (list): list of possible moves for users, used in validation of output.
                                elements of list must be stings

    Returns:
        str: element from list_of_options chosen by user
    """

    num_of_options_int = len(list_of_options)

    print(f'There are the following figure options:')
    for num, figure in enumerate(list_of_options, start=1):
        print(f'{num}. {figure}')

    prompt_for_player = f'Please, choose your figure by entering either figure number ' \
                        f'({1} to {num_of_options_int} as listed above) or full figure name: '

    while True:
        player_figure_input = input(prompt_for_player).lower().strip(' ')
        if player_figure_input.isdigit():

            if 1 <= int(player_figure_input) <= len(list_of_options):
                return list_of_options[int(player_figure_input) - 1]
            else:
                print(f'Error: number should be between {1} and {num_of_options_int}')

        elif player_figure_input in [figure.lower() for figure in list_of_options]:
            return player_figure_input.capitalize()

        else:
            print(
                f'Error: Input should be either a number between {1} and {num_of_options_int} '
                f'or valid figure name from the list above')



def get_ai_figure_random(list_of_options):
    """
     Returns random figure from the list of possible winning moves:
     Accepts list of possible winning moves and returns one random element of the list
     Args:
         list_of_options (list): list of possible moves.
     Returns:
         str: random element of list_of_options
     """
    return choice(list_of_options)


def get_round_resolution_from_ruleset(figure_1, figure_2, ruleset):
    """
    Defines the winner between two figures according to ruleset:
    Accept two figures, checks if combination exists in ruleset, decides which figure is a winner
    prints intermediary resolution results.

    Args:
        figure_1 (str): 1st input figure for resolution
        figure_2 (str): 1nd input figure for resolution
        ruleset (dict): dict of possible win figures combinations
                        {winner's figure : {loser's figure :
                        the way victor's figure overcome loser's figure}} -> Rock crushed Scissors
    Returns:
         int: int code of resolution outcome. 0 - draw, 1 - 1st figure 'wins', 2 - 2nd figure 'wins'
    """
    if figure_1 == figure_2:
        print(f'Resolution: both participants showed {figure_1}')
        return 0
    else:

        try:
            win_word = ruleset[figure_1][figure_2]
            print('-' * 40)
            print(f'Resolution: {figure_1} {win_word} {figure_2}')
            return 1
        except Exception:
            try:
                win_word = ruleset[figure_2][figure_1]
                print('-' * 40)
                print(f'Resolution: {figure_2} {win_word} {figure_1}')
                return 2
            except Exception as e:
                raise e


def battle_log_message(player_name, figure_name, mode):
    """
    Generates somewhat random battlelog entries to show Players' deep engagement into battle:
    accepts player name, figure name and mode
    mode allows to present different variants of messages

    Args:
        player_name (str): Name of player to be displayed in battlelog message
        figure_name (str): figure name to be displayed in battle-log message
        mode: variant of battlelog entry. Valid values:
                first_strike - message for first move among two
                riposte - message for response move among two

    Returns:
        str: stylized message of player showing particular figure
    """
    frases_dict = {'starters1': ['So', 'Initially', 'At first', 'At the very beginning'],
                   'midds12': [f'makes {figure_name} move', f'strikes with {figure_name}', f'shows {figure_name}'],
                   'starters2': ['But suddenly', 'But', 'After that', 'At the end of the day', 'While'],
                   'enders2': ['right off the bat', 'at the same time', 'like there is no tomorrow']
                   }
    if mode == 'first_strike':
        return f'{choice(frases_dict["starters1"])}, {player_name} {choice(frases_dict["midds12"])}'
    elif mode == 'riposte':
        return f'{choice(frases_dict["starters2"])}, {player_name} {choice(frases_dict["midds12"])} ' \
               f'{choice(frases_dict["enders2"])}'


def get_statistics_from_json_file(file_name):
    """
    Transforms json file to dict. If there is no json file, or no dict in it - returns empty dict

    Args:
        file_name: name of the file, from where function tries to get a dictionary from

    Returns:
        dict: dictionary converted from json
    """
    try:
        with open(file_name, 'rt') as file:
            output_dict = json_load(file)
            return output_dict
    except Exception as e:
        return {}


def save_statistics_to_json_file(file_name, dict_to_save):
    """
    Transforms dict to json file, so game statistics stores and accumulates between game session

    Args:
        file_name: name of the file, where function writes the dict keys/values
        dict_to_save: dict to be saved in the file

    Returns:
        file: file with name of  file_name where dict is written as key=value format
    """
    with open(file_name, 'wt') as file:
        json_to_save = json_dumps(dict_to_save)
        file.write(json_to_save)


def update_statistics(file_name, current_game_session_dict):
    """
    Updates (creates new file if neccessary) file_name statistics file with current game session results.
    Merges keys and summarize values of old dict and statistics of last game session
    Args:
        file_name (str): name of the file to update statistics in
        current_game_session_dict: dict of current game session kwargs, which contain statistics

    Returns:
        None
    """
    stat_to_update = get_statistics_from_json_file(file_name)
    if stat_to_update:
        stats_updated = {key: stat_to_update.get(key, 0) + current_game_session_dict.get(key, 0)
                         for key in set(stat_to_update).union(current_game_session_dict)}

    else:
        stats_updated = current_game_session_dict

    save_statistics_to_json_file(file_name, stats_updated)
    return


def srpls_the_game_main_function(player_1_name='Player_1', player_2_name='mr_AI',
                                 ruleset=win_cond_ruleset_dict, log_file_name='gamelog.txt',
                                 statistics_file_name='statistics.json'):
    """
    Manages the game of "rock scissors paper lizard spock" in general and prints progression messages as game goes.


    Args:
        player_1_name (str): name of 1st game participant - Player
                                Default value - 'Player_1'
        player_2_name (str): name of 2nd game participant - AI
                                Default value - 'mr_AI'
        ruleset (dict): dict of possible win figures combinations
                        {winner's figure : {loser's figure :
                        the way victor's figure overcome loser's figure}} -> Rock crushed Scissors
        log_file_name (srt): name of file where the log shall be written
        statistics_file_name (str): name of file where the games statistics shall be updated
    """
    valid_figures_list = list(ruleset.keys())

    current_game_statistics_dict = {'session_played': 1, 'rounds_played': 0,
                                    'wins': 0, 'loses': 0, 'draws': 0,
                                    }

    current_game_statistics_dict.update({key: 0 for key in valid_figures_list})

    with open(log_file_name, 'wt') as log_file:
        log_file.write(f'{datetime.now()} Log of the last game of \'rock scissors paper lizard spock\'. Game between '
                       f'player {player_1_name} and AI {player_2_name}\n')

        round_count = 1

        while True: # Loop for single round of the game

            # figure_of_player_1 = get_player_figure_input(valid_figures_list) # an alternative realizations
            figure_of_player_1 = selection_menu_input(f'Please, choose your figure:',valid_figures_list) # an alt realizations
            print(battle_log_message(player_name=player_1_name, figure_name=figure_of_player_1, mode='first_strike'))
            current_game_statistics_dict[figure_of_player_1] += 1

            figure_of_player_2 = get_ai_figure_random(valid_figures_list)
            print(battle_log_message(player_name=player_2_name, figure_name=figure_of_player_2, mode='riposte'))

            log_file.write(f'{datetime.now()} Round number {round_count}: '
                           f'{figure_of_player_1} vs {figure_of_player_2}, ')

            try:
                round_resolution_code = get_round_resolution_from_ruleset(figure_1=figure_of_player_1,
                                                                          figure_2=figure_of_player_2,
                                                                          ruleset=ruleset)
            except Exception as e:
                log_file.write(f'\n {e}')
                print(f'something went wrong: {e}')

            print('-' * 40)
            if round_resolution_code == 0:
                print(f'Result: a Draw')
                log_file.write(f'Round result: a Draw\n')
                current_game_statistics_dict['draws'] += 1
            elif round_resolution_code == 1:
                print(f'Result: {player_1_name} won')
                log_file.write(f'Round result: {player_1_name} won\n')
                current_game_statistics_dict['wins'] += 1
            elif round_resolution_code == 2:
                print(f'Result: {player_2_name} won')
                log_file.write(f'Round result: {player_1_name} won\n')
                current_game_statistics_dict['loses'] += 1
            else:
                log_file.write(f'Error. Round resolution failed for some strange reason')
                print(f'Can\'t resolve. Something went wrong. Lets try again')

            current_game_statistics_dict['rounds_played'] += 1
            print('-' * 40)
            next_round_decision = selection_menu_input('Another round?:', ['Yes', 'No and Exit'])

            if next_round_decision == 'Yes':
                round_count += 1
                print('-' * 40)
                print(f'Let\'s do another round then')
            elif next_round_decision == 'No and Exit':
                print('-' * 40)
                print(f'Exiting. Please check game log in {log_file_name} and player statistics in {statistics_file_name}')
                print('Thanks for your time. Have a nice day!')
                log_file.write(f'{datetime.now()} Exit: User decided to not proceed with the game')
                update_statistics(file_name=statistics_file_name, current_game_session_dict=current_game_statistics_dict)
                exit()
            else:
                return print('Error: Something unpredictable happened')


def selection_menu_input(menu_title, menu_options_list):
    """
    Function allows to choose one of the options with keyboard (Shift for previous selection,
    Ctrl for next selection, Alt for confirmation of current selection).
    Prints title from menu_title and list of options from the menu_options_list arguments. User chooses one of the
    options with Shift and Ctrl buttons and confirms selection with Alt button

    Args:
        menu_title: The title shown while selecting options
        menu_options_list (list): list of possible options to choose and later return

    Returns:
        str: one of elements from the menu_options_list
    """

    current_selection = 1
    list_length = len(menu_options_list)
    enum_list = list(enumerate(menu_options_list, start=1))

    def show_the_options_with_selection(prompt_to_show, enum_list_of_options):
        nonlocal current_selection
        print('\n')
        print(prompt_to_show)
        print('Please use -> UP <-, -> DOWN <- to go up and down, and -> Enter <- for confirmation of your choice')
        for num, element in enum_list_of_options:
            print(f'{"-->" if current_selection == num else "   "} '
                  f'{num}. {element} '
                  f'{"<--" if current_selection == num else "   "}')

    def one_up():
        nonlocal current_selection
        if current_selection == 1:
            return
        current_selection -= 1
        show_the_options_with_selection(menu_title, enum_list)

    def one_down():
        nonlocal current_selection
        if current_selection == list_length:
            return
        current_selection += 1
        show_the_options_with_selection(menu_title, enum_list)

    show_the_options_with_selection(menu_title, enum_list)
    add_hotkey('up', one_up)
    add_hotkey('down', one_down)

    keyboard_wait('enter')

    remove_hotkey('up')
    remove_hotkey('down')

    return enum_list[current_selection - 1][1]


def show_me_statistics(file_name='statistics.json', ruleset=win_cond_ruleset_dict):
    """
    Prints formatted text with statistics got from file_name file.
    Shows error message if fails to show statistics

    Args:
        file_name (str): Name of file where statistics is and shall be stored
        ruleset (dict): ruleset of a game as a dict


    """
    statistics = get_statistics_from_json_file(file_name)
    valid_list_of_moves = list(ruleset.keys())

    print('-' * 40)
    if not statistics:

        print('Unfortunately, there is nothing to show yet. Try playing the game')
    else:
        try:
            print(f'There were cumulatively {statistics["rounds_played"]} round played overall'
                  f' during {statistics["session_played"]} '
                  f'games sessions.\n'
                  f'Player won {statistics["wins"]} times, lost {statistics["loses"]} times, '
                  f'{statistics["draws"]} rounds ended with a draw')
        except KeyError:
            print('Unfortunately, there is no valid statistics stored')
        finally:
            print('-' * 40)

        for figure in valid_list_of_moves:
            if figure in statistics:
                print(f'{figure} played {statistics[figure]} times')




