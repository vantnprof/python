import pytest
import formatters as fmt


@pytest.fixture
def people():
    return [{
        "given": "Emma",
        "family": "Wilson",
        "role": "Engineer",
    }]


def test_display(people):
    assert fmt.format_people(people) == [
        "Emma Wilson: Engineer"
    ]


def test_csv(people):
    expected = (
        "given,family,role\n"
        "Emma,Wilson,Engineer\n"
    )
    assert fmt.export_csv(people) == expected


def test_empty_list():
    assert fmt.format_people([]) == []
