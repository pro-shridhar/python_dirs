import pytest
from add_num import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("91", "19", "110"),
        ("123456789", "987654322", "1111111111"),
        ("9999999", "1", "10000000"),
        ("300", "3000", "3300"),
        ("1000", "6200", "7200"),
        ("-10", "-20", "-30"),
        ("-100", "100", "0"),
        ("0", "6200", "6200"),
        ("", "6", "Invalid Operation"),
        ("", None, "Invalid Operation"),
        (None, "23", "Invalid Operation"),
        ("", "20", "Invalid Operation"),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
