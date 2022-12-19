from library import GamesSettingsSingleton
from library import GameScreens
from library import HumanPlayer
from library import AiPlayer
from library import GameSession
from json import load as json_load

sett = GamesSettingsSingleton()
screens = GameScreens(sett)
ai = AiPlayer(sett)
human = HumanPlayer(sett)
game_session = GameSession(sett)


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
