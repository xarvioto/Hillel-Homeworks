# Візьміть гру з попереднього ДЗ ('rock scissors paper lizard spock') і модифікуйте наступним чином:
# винесіть всі функції в окремий файл (нехай буде library.py) і імпортуцте їх звідти для роботи в основний файл
# додайте запис статистики в файл (які фігури грали і хто переміг на кожному ході), використовуйте open.

from library import srpls_the_game_main_function
from library import selection_menu_input
from library import show_me_statistics
from library import exiting_procedure

main_menu_functions_dict = {'Play the game': srpls_the_game_main_function,
                            'Show accumulative statistics till now': show_me_statistics,
                            'Exit the game': exiting_procedure
                            }
"""
Dict of functions to execute after correspondent main menu element is chosen
"""


if __name__ == '__main__':
    while True:
        menu_point_selected = selection_menu_input('Main menu for \'rock scissors paper lizard spock\' game',
                                                   list(main_menu_functions_dict.keys()))
        function_to_execute = main_menu_functions_dict[menu_point_selected]
        function_to_execute()














