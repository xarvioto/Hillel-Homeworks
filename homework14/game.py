# Візьміть свою гру з HW8 і перепишіть ії в обʼєктному стилі. Зробіть максимум взаємодії (як явної так і неявної) на
# рівні обʼєктів. Рекомендую подумати над такими класами як Player, GameFigure, Game. Памʼятайте про чистоту і
# простоту коду (DRY, KISS), коментарі та докстрінги.

from library import GamesSettingsSingleton
from library import GameScreens
from library import HumanPlayer
from library import AiPlayer
from library import GameSession
from json import load as json_load

sett = GamesSettingsSingleton()

# all four have single parameter: GamesSettingsSingleton object. You can pass sett instead - it will have no difference
# unless you pass other instance with similar interface but different implementation
# all of the following expect some kind of object that will grant references to all the other objects
screens = GameScreens()
ai = AiPlayer()
human = HumanPlayer()
game_session = GameSession()

def play_the_game():
    """
    Start a session of the game
    """
    with game_session:
        game_session.play_game_session()


def show_statistics():
    """
    Show function. Reveals, that statistics carries on through the different game sessions.
    """
    try:
        with open('statistics.txt', 'rt') as file:
            print('State of statistics.txt file after the game session')
            print(json_load(file))
    except FileNotFoundError as e:
        print('There is no statistics.txt file yet. Please play the game first')


if __name__ == "__main__":
    play_the_game()
    show_statistics()








