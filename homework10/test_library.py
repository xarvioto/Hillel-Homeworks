import pytest
from library import make_positive_power_of_two_real_nums_product


def test_calc_logic_for_make_positive_power_of_two_real_nums_product():
    assert make_positive_power_of_two_real_nums_product(-2, 3, power_num=2) == 36, 'not expected result'

    assert make_positive_power_of_two_real_nums_product(1, 2, power_num=3) == 8, 'not expected result'
    assert make_positive_power_of_two_real_nums_product(2, -3, power_num=3) == -216, 'not expected result'
    assert make_positive_power_of_two_real_nums_product(2, 3, power_num=0) == 1, 'not expected result'
    assert make_positive_power_of_two_real_nums_product(0, 0, power_num=5) == 0, 'not expected result'


def test_result_type_for_make_positive_power_of_two_real_nums_product():
    assert type(make_positive_power_of_two_real_nums_product(2, 4, power_num=5)) == int, 'not expected result type'
    assert type(make_positive_power_of_two_real_nums_product(1.5, 2, power_num=3)) == float, 'not expected result type'
    assert type(make_positive_power_of_two_real_nums_product(1, 2.5, power_num=3)) == float, 'not expected result type'
    assert type(make_positive_power_of_two_real_nums_product(1, 2, power_num=3.5)) == float, 'not expected result type'


def test_args_kwargs_typeerror_for_make_positive_power_of_two_real_nums_product():
    with pytest.raises(TypeError):
        make_positive_power_of_two_real_nums_product(2, 3, 4)

    with pytest.raises(TypeError):
        make_positive_power_of_two_real_nums_product(2, factor_num_one=3, power_num=4)


def test_num_types_typeerror_for_make_positive_power_of_two_real_nums_product():
    with pytest.raises(TypeError):
        make_positive_power_of_two_real_nums_product('2', 3, power_num=4)

    with pytest.raises(TypeError):
        make_positive_power_of_two_real_nums_product(2, 3+4j, power_num=4)

    with pytest.raises(TypeError):
        make_positive_power_of_two_real_nums_product(2, 3, power_num=[4])


def test_negative_power_valueerror_for_make_positive_power_of_two_real_nums_product():
    with pytest.raises(ValueError):
        make_positive_power_of_two_real_nums_product(3, 4, power_num=-5)
