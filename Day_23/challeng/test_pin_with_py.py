import pytest
from valid_pin import valid


@pytest.mark.parametrize(
    "pin,result",
    [
        ("123456", True),
        ("4512a5", False),
        ("", False),
        ("21904", False),
        ("9451", True),
        ("213132", True),
        (" 4520", False),
        ("15632 ", False),
        ("000000", True),
    ],
)
def test_pin(pin, result):
    assert valid(pin) == result
