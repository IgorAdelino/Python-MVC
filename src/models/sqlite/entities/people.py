from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, BIGINT, String


class PeopleTable(Base):
  __tablename__ = "people"

  id = Column(BIGINT, primary_key=True)
  first_name = Column(String, nullable=False)
  last_name = Column(String, nullable=False)
  age = Column(BIGINT, nullable=False)
  pet_id = Column(BIGINT, foreign_key="pets.id")

  def __repr__(self):
    return f"People [id={self.id}, name={self.first_name} {self.last_name}, age={self.age}]"

  