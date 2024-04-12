from myproject.main import division
import pytest


@pytest.mark.parametrize("num_1, num_2, expected", [(10, 2, 5),
                                                    (20, 10, 2),
                                                    (33, 11, 3)])
def test_division(num_1, num_2, expected):
    assert division(num_1, num_2) == expected
