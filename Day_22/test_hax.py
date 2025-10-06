import pytest
from hax_binary import to_binary


@pytest.mark.parametrize(
    "input_hex, expected",
    [
        (0xFF, "11111111"),
        (0xAA, "10101010"),
        (0xFA, "11111010"),
    ],
)
def test_to_binary(input_hex, expected):
    assert to_binary(input_hex) == expected
