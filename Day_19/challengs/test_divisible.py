import pytest

from devisible_by_b import divisible_by_b


@pytest.mark.parametrize(
    "n, b, expected",
    [
        (17, 8, 24),
        (98, 3, 99),
        (14, 11, 22),
        (11, 8, 16),
        (450, 36, 468),
        (1019, 13, 1027),
    ],
)
def test_divisible_by_b(n, b, expected):
    assert divisible_by_b(n, b) == expected
