import functools
from typing import Annotated
from annotated_types import Ge


@functools.cache
def make_positive_power_of_two_real_nums_product(factor_num_one: int | float,
                                                 factor_num_two: int | float,
                                                 /,
                                                 *,
                                                 power_num: Annotated[int, Ge(0)]) -> int | float:
    int_n_float_set = {int, float}

    if not type(factor_num_one) in int_n_float_set \
            or not type(factor_num_two) in int_n_float_set \
            or not type(power_num) == int:
        raise TypeError

    if power_num < 0:
        raise ValueError

    return (factor_num_one * factor_num_two) ** power_num
