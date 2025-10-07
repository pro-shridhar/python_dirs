import pytest
from invert_dct import invert


@pytest.mark.parametrize(
    "input_dict,expected_output",
    [
        ({"a": 1, "b": 2, "c": 3}, {1: "a", 2: "b", 3: "c"}),
        ({"z": "q", "w": "f"}, {"q": "z", "f": "w"}),
        ({"zebra": "koala", "horse": "camel"}, {"koala": "zebra", "camel": "horse"}),
    ],
)
def test_invert(input_dict, expected_output):
    assert invert(input_dict) == expected_output
