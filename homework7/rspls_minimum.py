# 1. Напишіть гру "rock scissors paper lizard spock". Використайте розділення всієї програми на функції (
# Single-Responsibility principle). Як скелет-заготовку можна використати приклад з заняття.

# 2. До кожної функції напишіть докстрінг або анотацію

# https://www.youtube.com/watch?v=_PUEoDYpUyQ

from random import choice

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
    Accepts as arguments a list of possible moves
    Displays all possible options to user.
    Allows input as wither number of move, or full name of figure
    Validates the input
    Repeats request for input if gets invalid input
    Returns chosen and validated figure name as str

    Args:
        list_of_options: list
    Returns:
        str
    """

    num_of_options_int = len(list_of_options)

    print(f'There are the following figure options:')
    [print(f'{i + 1}. {list_of_options[i]}') for i in range(num_of_options_int)]
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
        list_of_options: list
    Returns:
        str
    """
    return choice(list_of_options)


def get_round_resolution_from_ruleset(figure_1, figure_2, ruleset):
    """
    Defines the winner between two figures according to ruleset:
    Accept two figures, checks if combination exists in ruleset, decides which figure is a winner
    prints intermediary resolution results.

    Valid outcomes:
        0 - draw, both figures are the same
        1 - 1st figure 'wins'
        2 - 2nd figure 'wins'

    Args:
        figure_1 : str
        figure_2 : str
        ruleset : dict
    Returns:
         int
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
        except:
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
        parameter mode have 2 valid values (as there are two types of battlelog entries): first_stike, riposte
    Args:
        player_name: str
        figure_name: str 
        mode: str

    Returns:
        str
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

def srpls_the_game_main_function(player_1_name='Player_1', player_2_name='mr_AI',
                                 ruleset=win_cond_ruleset_dict):
    """
    Manages the game of "rock scissors paper lizard spock" in general and prints progression messages as game goes.
    Accepts ruleset and players names, calls input functions for both players, call resolution function and prints
    results.
    In case of a Draw - repeats until somebody wins, 'cause it is either human or AI, draw is not an option.

    Args:
        player_1_name: str
        player_2_name: str
        ruleset : dict
    Returns:
        print? None? In reality it returns print functions with some parameters
    """
    valid_figures_list = list(ruleset.keys())

    while True:
        figure_of_player_1 = get_player_figure_input(valid_figures_list)
        print(battle_log_message(player_name=player_1_name, figure_name=figure_of_player_1, mode='first_strike'))

        figure_of_player_2 = get_ai_figure_random(valid_figures_list)
        print(battle_log_message(player_name=player_2_name, figure_name=figure_of_player_2, mode='riposte'))

        try:
            round_resolution_code = get_round_resolution_from_ruleset(figure_1=figure_of_player_1,
                                                                      figure_2=figure_of_player_2,
                                                                      ruleset=ruleset)
        except Exception as e:
            print(f'something went wrong: {e}')  # should never happen

        print('-' * 40)
        if round_resolution_code == 0:
            print(f'Result: a Draw. Lets try again')
            print('-' * 40)
        elif round_resolution_code == 1:
            return print(f'Result: {player_1_name} won')  # return here is to exit the function
        elif round_resolution_code == 2:
            return print(f'Result: {player_2_name} won')  # return here is to exit the function
        else:
            return print(f'Can\'t resolve. Something went wrong. Lets try again')  # should never happen


srpls_the_game_main_function()
