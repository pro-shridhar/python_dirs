import pytest
from binary import k_th_binary_inlist


@pytest.mark.parametrize(
    "k, n, expected",
    [
        (3, 5, "0b1"),
        (4, 10, "0b1010"),
        (5, 16, "0b11100"),
        (10, 5, "0b1110111111"),
        (7, 10, "0b101111"),
    ],
)
def test_k_th_binary_inlist(k, n, expected):
    assert k_th_binary_inlist(k, n) == expected
