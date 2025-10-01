import pytest
from date_for import format_date


@pytest.mark.parametrize(
    "input_date, expected_output",
    [
        ("11/12/2019", "20191211"),
        ("12/31/2019", "20193112"),
        ("01/15/2019", "20191501"),
    ],
)
def test_format_date(input_date, expected_output):
    assert format_date(input_date) == expected_output
