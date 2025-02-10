from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Database interaction test")
def test_list_pets():
  repo = PetsRepository(db_connection_handler)
  
  response = repo.list_pets()

def test_delete_pet():
  repo = PetsRepository(db_connection_handler)

  response =repo.delete_pet(1)
  print(response)
