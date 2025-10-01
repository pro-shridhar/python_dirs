import pytest
from check_friday import has_friday_13


@pytest.mark.parametrize(
    "month, year, expected",
    [
        (3, 2020, True),
        (10, 2017, True),
        (1, 1985, False),
        (5, 1619, False),
        (6, 1614, True),
        (8, 1767, False),
        (6, 1589, False),
        (2, 2015, True),
        (3, 2015, True),
        (11, 2015, True),
        (2, 1759, False),
        (8, 1612, False),
        (8, 1612, False),  # Duplicate kept for completeness
        (10, 2029, False),
        (1, 1590, False),
        (7, 1812, False),
        (1, 1785, False),
        (11, 1961, False),
        (9, 1706, False),
        (5, 2016, True),
        (11, 2020, True),
        (1, 2023, True),
        (10, 2023, True),
        (2, 2043, True),
        (4, 2043, False),
        (3, 2043, True),
        (11, 2043, True),
    ],
)
def test_has_friday_13(month, year, expected):
    assert has_friday_13(month, year) == expected
