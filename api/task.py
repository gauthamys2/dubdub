from sqlalchemy import Column, String, Boolean
from base import Base

class Task(Base):
    __tablename__ = 'tasks'
    name = Column(String, primary_key=True)
    completed = Column(Boolean, default=False)

    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed