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
        print(f'Resolution: both partisipants showed {figure_1}')
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


def srpls_the_game_main_function(player_1_name='Monsieur_ROBOT', player_2_name='mr_AI', input_1_func=get_ai_figure_random,
                                 input_2_func=get_ai_figure_random, ruleset=win_cond_ruleset_dict):
    """
    Manages the game of "rock scissors paper lizard spock" in general and prints progression messages as game goes.
    Accepts ruleset, players names, input fucntions, calls input functions for both players, call resolution function and prints
    results.
    input_1_func and input_2 _func functions as parameters for getting input figuresa allow different game modes like:
    Player vs AI, Player vs Player, AI vs AI, cheatmode: AI vs Player
    In case of a Draw - repeats until somebody wins, 'cause it is either human or AI, draw is not an option.

    Args:
        player_1_name: str
        player_2_name: str
        input_1_func : func
        input_2_func : func
        ruleset : dict
    Returns:
        print? None?
    """
    valid_figures_list = list(ruleset.keys())

    while True:
        figure_of_player_1 = input_1_func(valid_figures_list)
        print(f'So, {player_1_name} makes {figure_of_player_1} move')

        figure_of_player_2 = input_2_func(valid_figures_list)
        print(f'while {player_2_name} shows {figure_of_player_2} at the same time')

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
