import pytest

from library import GameRulesSet


def test_game_rules_set_positive_init_and_getting():
    win_cond_dict_1 = {'move_1': {'move_2': 'win_word_2', 'move_3': ''},
                       'move_2': {'move_3': 'win_word_3'},
                       'move_3': {}
                       }
    test_rules_set = GameRulesSet(win_cond_dict_1)

    assert str(test_rules_set) == str(win_cond_dict_1)
    assert test_rules_set.move_1.move_1.resolution == 'draw'
    assert test_rules_set.move_1.move_2.resolution == 'win'
    assert test_rules_set.move_1.move_3.resolution == 'win'
    assert test_rules_set.move_1.move_2.win_word == 'win_word_2'

    # emtpy or '' win_word in rules should be substituted with default value 'overcomes'
    assert test_rules_set.move_1.move_3.win_word == 'overcomes'

    assert test_rules_set.move_2.move_1.resolution == 'lose'
    assert test_rules_set.move_2.move_2.resolution == 'draw'
    assert test_rules_set.move_2.move_3.resolution == 'win'
    assert test_rules_set.move_2.move_3.win_word == 'win_word_3'

    assert test_rules_set.move_3.move_1.resolution == 'lose'
    assert test_rules_set.move_3.move_2.resolution == 'lose'
    assert test_rules_set.move_3.move_3.resolution == 'draw'


def test_game_rules_set_errors():
    win_cond_dict_1 = {'move_1': {'move_1': 'win_word_1'},
                       'move_2': {'move_3': 'win_word_3'},
                       'move_3': {}
                       }

    with pytest.raises(ValueError):  # win_condition dict must not be empty
        win_cond_dict_1 = {}
        test_rules_set = GameRulesSet(win_cond_dict_1)

    with pytest.raises(ValueError):  # self move must be a draw, must not be present as a winning condition
        win_cond_dict_1 = {'move_1': {'move_1': 'win_word_1'}
                           }
        test_rules_set = GameRulesSet(win_cond_dict_1)

    with pytest.raises(ValueError):  # finds two conflicting winning conditions, 1 wins 2, and 2 wins 1 simultaneously
        win_cond_dict_2 = {'move_1': {'move_2': 'win_word_1'},
                           'move_2': {'move_1': 'win_word_1'}
                           }
        test_rules_set = GameRulesSet(win_cond_dict_2)

    with pytest.raises(ValueError):  # there is a losing move move_3 that is not present in the list of winning moves
        win_cond_dict_3 = {'move_1': {'move_2': 'win_word_1'},
                           'move_2': {'move_3': 'win_word_1'}
                           }
        test_rules_set = GameRulesSet(win_cond_dict_3)
