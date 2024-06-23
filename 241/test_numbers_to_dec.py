import pytest

from numbers_to_dec import list_to_decimal

test_sample = {
    's1' : ([0, 4, 2, 8], 428),
    's2' : ([1, 2], 12),
    's3' : ([3], 3),
    's4' : ([6, 2, True], 'TypeError'),
    's5' : ([-3, 12], 'ValueError'),
    's6' : ([3.6, 4, 1], 'TypeError'),
    's7' : (['4', 5, 3, 1], 'TypeError')
    's8' : ([12], 'ValueError'),
}
def test_numbers_to_dec():
    for k, v in test_sample.items():
        actual = list_to_decimal(v[0])
        expected = v[1]
        return actual == expected



