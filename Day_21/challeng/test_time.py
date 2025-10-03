import pytest
from time_save import time_saved


@pytest.mark.parametrize(
    "speed1, speed2, distance, expected",
    [
        (80, 90, 40, 3.3),
        (80, 90, 4000, 333.3),
        (80, 100, 40, 6.0),
        (80, 100, 10, 1.5),
        (60, 65, 25, 1.9),
        (60, 60, 20, 0),
        (80, 95, 200, 23.7),
        (70, 92, 50, 10.2),
        (70, 92, 20, 4.1),
        (70, 100, 12, 3.1),
    ],
)
def test_time_saved(speed1, speed2, distance, expected):
    result = time_saved(speed1, speed2, distance)
    assert result == expected, (
        f"time_saved({speed1}, {speed2}, {distance}) "
        f"expected {expected}, got {result}"
    )
