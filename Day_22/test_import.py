import pytest
from import_str import fix_import


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("import object from module_name", "from module_name import object"),
        ("import randint from random", "from random import randint"),
        ("import pi from math", "from math import pi"),
    ],
)
def test_fix_import(input_str, expected):
    assert fix_import(input_str) == expected
