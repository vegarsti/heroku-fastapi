from sqlalchemy import Column, Integer, String

from .database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, unique=True, index=True)
