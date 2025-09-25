import pytest


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


def format_data_for_display(people):
    return [f"{p['given_name']} {p['family_name']}: {p['title']}" for p in people]


def format_data_for_excel(people):
    lines = ["given,family,title"]
    for person in people:
        lines.append(
            f"{person['given_name']},{person['family_name']},{person['title']}"
        )
    return "\n".join(lines) + "\n"


def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


@pytest.mark.excel_format
def test_format_data_for_excel(example_people_data):
    assert (
        format_data_for_excel(example_people_data)
        == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""
    )


@pytest.fixture
def example_fixture():
    return 1


def test_with_fixture(example_fixture):
    assert example_fixture == 1
