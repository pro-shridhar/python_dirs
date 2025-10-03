import pytest
from avg import ave_spd


@pytest.mark.parametrize(
    "uphill_speed, downhill_speed, time, expected",
    [
        (18, 10, 30, 15),
        (18, 20, 60, 30),
        (30, 10, 30, 15),
        (30, 8, 24, 12),
    ],
)
def test_ave_spd(uphill_speed, downhill_speed, time, expected):
    result = ave_spd(uphill_speed, downhill_speed, time)
    assert result == expected, (
        f"ave_spd({uphill_speed}, {downhill_speed}, {time}) "
        f"expected {expected}, got {result}"
    )
