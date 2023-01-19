from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from db_conf import Base

class Task(Base):
    __tablename__="task"

    id = Column(Integer, primary_key=True, index=True)
    Title= Column(String)
    Description= Column(String)
    Time= Column(DateTime(timezone=True), server_default=func.now())
    image=Column(String)
