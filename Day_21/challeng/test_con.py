import pytest
from consecutive import consecutive_combo


@pytest.mark.parametrize(
    "lst1, lst2, expected",
    [
        ([1, 4, 5, 7], [2, 3, 6], True),
        ([1, 4, 5, 6], [2, 7, 8, 9], False),
        ([1, 4, 5, 6], [2, 3, 7, 8, 10], False),
        ([7, 5, 4, 1], [2, 3, 6, 8], True),
        ([33, 34, 40], [39, 38, 37, 36, 35, 32, 31, 30], True),
        ([1, 4, 5, 6], [2, 3, 7, 8, 10], False),
        ([44, 46], [45], True),
        ([4, 3, 1], [2, 5], True),
        ([4, 3, 1], [2, 5, 7, 6], True),
        ([4, 3, 1], [7, 6, 5], False),
        ([4, 3, 1], [0, 7, 6, 5], False),
        ([44, 46], [45], True),
    ],
)
def test_consecutive_combo(lst1, lst2, expected):
    result = consecutive_combo(lst1, lst2)
    assert (
        result == expected
    ), f"consecutive_combo({lst1}, {lst2}) expected {expected}, got {result}"
