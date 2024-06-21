from fibonacci import fib
import pytest

# write one or more pytest functions below, they need to start with test_
def test_fib():
    test_matrix = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
        4: 3,
        5: 5,
        6: 8,
        7: 13,
        8: 21
    }

    for k, v in test_matrix.items():
        actual = fib(k)
        expected = v

        assert actual == expected

def test_fib_num_negative():
    with pytest.raises(ValueError):
        fib(-2)
