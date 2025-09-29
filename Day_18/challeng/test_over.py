import pytest
from total_over import total_overs


@pytest.mark.parametrize(
    "over, result",
    [
        (2400, 400),
        (164, 27.2),
        (945, 157.3),
        (5, 0.5),
        (7, 1.1),
        (15, 2.3),
        (0, 0),
    ],
)
def test(over, result):
    assert total_overs(over) == result
