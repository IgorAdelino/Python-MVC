from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Database interaction test")
def test_list_pets():
  repo = PetsRepository(db_connection_handler)
  
  response = repo.list_pets()

@pytest.mark.skip(reason="Database interaction test")
def test_delete_pet():
  repo = PetsRepository(db_connection_handler)

  response = repo.delete_pet(1)
  print(response)

def test_insert_person():
  first_name = "test_name"
  last_name = "test_last_name"
  age = 23
  pet_id = 1
  repo = PeopleRepository(db_connection_handler)
  
  response = repo.insert_person(first_name, last_name, age, pet_id)
  print(response)
