import pytest
from src import Person

@pytest.fixture()
def person():
    return Person("Dominik Salabura", 22)

def test_person(person: Person):
    assert person.forname == "Dominik"
    assert person.surname == "Salabura"
    assert person.age == 22

def test_celebrate_birthday(person: Person):
    assert person.age == 22
    person.celebrate_birthsday()
    assert person.age == 23