from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import DECIMAL
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func

from course.alfredo.pyside.kardex.app.config.db import Base


class Operation(Base):
    __tablename__ = "operations"

    id = Column(Integer, primary_key=True, autoincrement=True)

    company = Column(String(150), nullable=False)
    account_number = Column(String(50), nullable=False)
    issuer = Column(String(150), nullable=False)
    operation = Column(String(100), nullable=False)
    movement_date = Column(Date, nullable=False)
    instrument = Column(String(150), nullable=False)

    quantity = Column(DECIMAL(18, 4), nullable=False)
    price = Column(DECIMAL(18, 4), nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())