from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.sql.sqltypes import Float, PickleType

from app.database import Base


class User(Base):
    """Creates a table with an SQLAlchemy model to store user information

    :attr __tablename__: The name of the table, "user"
    :type __tablename__: str
    :param id: Creates a column named "id" to store the id of each user
    :type id: Integer
    :param username: Creates a column named "username" to store the username
    of each user associated with each "id"
    :type username: String
    :param username: Creates a column named "password" to store the
    password of each user associated with each "id"
    :type id: String
    :param id: Creates a column named "created_at" to store the time of
    creation for each user associated with each "id"
    :type id: Float
    """

    __tablename__ = "user"

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    created_at = Column(Float)

    QR: RelationshipProperty = relationship("QR", back_populates="user")


class QR(Base):
    __tablename__ = "QR"

    id = Column(Integer, index=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    created_at = Column(Float)
    title = Column(String)
    link = Column(String)

    user: RelationshipProperty = relationship("User", back_populates="QR")
