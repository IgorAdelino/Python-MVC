from typing import List
from src.models.sqlite.entities.people import PeopleTable
from sqlalchemy.orm.exc import NoResultFound

class PeopleRepository:
  def __init__(self, db_connection):
    self.__db_connection = db_connection

  
  def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
    with self.__db_connection as database:
      try:
        person_data = PeopleTable (
          first_name=first_name,
          last_name=last_name,
          age=age,
          pet_id=pet_id
        )
        database.session.add(person_data)
        database.session.commit()
      except Exception as exception:
        database.session.rollback()
        raise exception