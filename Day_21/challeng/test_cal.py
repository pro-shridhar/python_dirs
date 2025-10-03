import pytest
from calculator import Calculator


@pytest.mark.parametrize(
    "method, a, b, expected",
    [
        ("add", 5, 5, 10),
        ("add", 20, 5, 25),
        ("subtract", 30, 5, 25),
        ("subtract", 100, 5, 95),
        ("multiply", 5, 5, 25),
        ("multiply", 100, 5, 500),
        ("divide", 10, 5, 2),
        ("divide", 100, 5, 20),
    ],
)
def test_calculator(method, a, b, expected):
    calculator = Calculator()
    result = getattr(calculator, method)(a, b)
    assert result == expected, f"{a} {method} {b} should be {expected}, got {result}"
