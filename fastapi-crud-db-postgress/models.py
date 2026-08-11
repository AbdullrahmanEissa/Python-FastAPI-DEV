from sqlalchemy import Column, Integer, String, Text
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)