import pytest
from frection_value import frection_value


def test_value():
    assert frection_value(23.345) == "4669/200"


def test_complete_value():
    with pytest.raises(ValueError):
        assert frection_value(3443.00)
