from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime, JSON, Text, UniqueConstraint
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    event_id = Column(String, unique=True, index=True)
    label = Column(String)
    metadata = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    event = Column(String, index=True)
    qid = Column(Integer)
    text = Column(Text)
    choices = Column(JSON)
    answer = Column(String)
    topic = Column(String, index=True)
    subtopic = Column(String, index=True)

class Mastery(Base):
    __tablename__ = "mastery"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    event = Column(String, index=True)
    topic = Column(String, index=True)
    subtopic = Column(String, index=True)
    prob = Column(Float, default=0.0)
    __table_args__ = (UniqueConstraint('user_id','event','topic','subtopic', name='uix_user_event_topic_sub'),)
