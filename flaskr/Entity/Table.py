import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import REAL, Column, Integer, Table, String, DateTime, ForeignKey, LargeBinary, Numeric, \
    SmallInteger, Text, NVARCHAR, VARCHAR, Date, Boolean
from sqlalchemy.dialects.postgresql import BIT, DOUBLE_PRECISION, REAL, ARRAY
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative.api import DeclarativeMeta

base = declarative_base()

def getTableBase() -> DeclarativeMeta:
    return base

class CardPoolEntity(base):
    __tablename__ = 'CardPool'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column('id', Integer, primary_key = True, autoincrement = True)
    name = Column('name', VARCHAR(20), nullable = True)
    describe = Column('describe', Text, nullable = False)
    userId = Column('userId', Text, nullable = False)
    isPublic = Column('isPublic', Boolean, nullable = False, default = False)

class CardEntity(base):
    __tablename__ = 'Card'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    id = Column('id', Integer, primary_key = True, autoincrement = True)
    cardPoolId = Column('cardPoolId', Integer, ForeignKey('CardPool.id'), nullable = False)
    userId = Column('userId', Text, nullable = False)
    name = Column('name', VARCHAR(20), nullable = True)
    image = Column('image', Text, nullable = False)
    weight = Column('weight', Integer, nullable = False)