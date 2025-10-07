import pytest
from full_name import Employee


@pytest.mark.parametrize(
    "first, last, fullname, email",
    [
        ("John", "Smith", "John Smith", "john.smith@company.com"),
        ("Mary", "Sue", "Mary Sue", "mary.sue@company.com"),
        ("Antony", "Walker", "Antony Walker", "antony.walker@company.com"),
        ("Joshua", "Senoron", "Joshua Senoron", "joshua.senoron@company.com"),
    ],
)
def test_employee(first, last, fullname, email):
    emp = Employee(first, last)
    assert emp.firstname == first
    assert emp.lastname == last
    assert emp.fullname == fullname
    assert emp.email == email
