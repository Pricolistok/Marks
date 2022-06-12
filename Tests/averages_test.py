from Controller.journal.get_average import get_average, get_averages


def test_average():
    assert get_average([4, 5, 6]) == 5.0


def test_empty_average():
    assert get_average([]) == 0.0


def test_float_average():
    assert get_average([5, 4, 4]) == 4.33


def test_long_average():
    assert get_average([2, 3, 7, 1, 22, 5, 4, 3, 12, 3, 8, 4, 17, 8]) == 7.07


def test_many_averages():
    assert get_averages({"1": [1, 2, 3], "2": [], "3": [0, 1, 1]}) == {"1": 2.0, '2': 0.0, "3": 0.67}
