from unittest import mock
from .pets_repository import PetsRepository
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable

class MockConnection:
  def __init__(self) -> None:
    self.session = UnifiedAlchemyMagicMock(
      data=[
        (
          [mock.call.query(PetsTable)], #Query
          [
            PetsTable(name= "cao", type= "dog"), 
            PetsTable(name= "gato", type= "cat")
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
  print(response)
  assert response[0].name == "cao"
  