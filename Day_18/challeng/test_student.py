import pytest
from get_st8udent import top_note


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ({"name": "Jacek", "notes": [5, 4, 3]}, {"name": "Jacek", "top_note": 5}),
        ({"name": "Ewa", "notes": [3, 3, 3]}, {"name": "Ewa", "top_note": 3}),
        ({"name": "Zygmund", "notes": [1, 2, 3]}, {"name": "Zygmund", "top_note": 3}),
        ({"name": "Alex", "notes": [1, 4, 6]}, {"name": "Alex", "top_note": 6}),
    ],
)
def test_top_note(input_data, expected):
    assert top_note(input_data) == expected
