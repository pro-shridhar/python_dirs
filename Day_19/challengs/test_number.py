import pytest

from disarium_number import is_disarium


@pytest.mark.parametrize(
    "num, expected",
    [
        (6, True),
        (75, False),
        (135, True),
        (466, False),
        (372, False),
        (175, True),
        (1, True),
        (696, False),
        (876, False),
        (89, True),
        (518, True),
        (598, True),
    ],
)
def test_is_disarium(num, expected):
    assert is_disarium(num) == expected
