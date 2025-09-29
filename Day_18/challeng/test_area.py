import pytest
from Day_18.challeng.circle_square import square_areas_difference


@pytest.mark.parametrize(
    "radius, expected",
    [
        (5, 50),
        (6, 72),
        (7, 98),
        (17, 578),
    ],
)
def test_square_areas_difference(radius, expected):
    assert square_areas_difference(radius) == expected
