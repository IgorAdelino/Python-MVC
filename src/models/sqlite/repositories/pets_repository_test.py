from unittest import mock
from .pets_repository import PetsRepository
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
import pytest


class MockConnection:
  def __init__(self) -> None:
    self.session = UnifiedAlchemyMagicMock(
      data=[
        (
          [mock.call.query(PetsTable)], #Query
          [
            PetsTable(id= 1, name= "cao", type= "dog"), 
            PetsTable(id=2, name= "gato", type= "cat")
          ] #Result
        )
      ]
    )
  def __enter__(self):
      return self
  def __exit__(self, exc_type, exc_value, traceback):
      pass

def test_list_pets():
  mock_connection = MockConnection()
  repo = PetsRepository(mock_connection)
  response = repo.list_pets()

  mock_connection.session.query.assert_called_once_with(PetsTable)
  mock_connection.session.all.assert_called_once()
  mock_connection.session.filter.assert_not_called()

  assert response[0].name == "cao"

def test_delete_pet():
   mock_connection = MockConnection()
   repo = PetsRepository(mock_connection)

   repo.delete_pet(1)

   mock_connection.session.query.assert_called_once_with(PetsTable)
   mock_connection.session.filter.assert_called_once_with(PetsTable.id == 1)
   mock_connection.session.delete.assert_called_once()

  