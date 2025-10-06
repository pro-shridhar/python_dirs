import pytest
from ascii import to_dict


@pytest.mark.parametrize(
    "input_list, expected",
    [
        (["a", "b", "c"], [{"a": 97}, {"b": 98}, {"c": 99}]),
        (["!", ".", "?"], [{"!": 33}, {".": 46}, {"?": 63}]),
        (["^"], [{"^": 94}]),
        ([" "], [{" ": 32}]),
        ([], []),
    ],
)
def test_to_dict(input_list, expected):
    assert to_dict(input_list) == expected
