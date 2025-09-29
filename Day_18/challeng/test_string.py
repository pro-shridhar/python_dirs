import pytest
from string_number import arithmetic_operation


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("12 + 12", 24),
        ("22 - 12", 10),
        ("100 * 12", 1200),
        ("120 // 10", 12),
        ("122 // 0", -1),  # Handle division by zero
        ("10 * 20", 200),
        ("10 - 10", 0),
        ("10 - 12", -2),
    ],
)
def test_operation(expression, expected):
    assert arithmetic_operation(expression) == expected
