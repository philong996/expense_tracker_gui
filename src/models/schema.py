from sqlalchemy import create_engine, Column, Integer, String, Float, Text, Date, ForeignKey, Table, CheckConstraint, DECIMAL, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()
DATABASE_URL = "postgresql+psycopg2://postgres:changeme@localhost/expense_gui"
# DATABASE_URL = "sqlite:///expense_tracker.db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class User(Base):
    """ User model"""
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), CheckConstraint("role IN ('admin', 'user')"), default='user')
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    expenses = relationship('Expense', back_populates='user')
    user_groups = relationship('UserGroup', back_populates='user')

class Group(Base):
    """ Group model"""
    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(100), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    user_groups = relationship('UserGroup', back_populates='group')
    expenses = relationship('Expense', back_populates='group')

class UserGroup(Base):
    """ UserGroup model"""
    __tablename__ = 'user_group'

    user_group_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.group_id', ondelete='CASCADE'), nullable=False)
    role = Column(String(20), CheckConstraint("role IN ('owner', 'member')"), default='member')

    user = relationship('User', back_populates='user_groups')
    group = relationship('Group', back_populates='user_groups')

class Category(Base):
    """ Category model"""
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    expenses = relationship('Expense', back_populates='category')

class Expense(Base):
    """ Expense model"""
    __tablename__ = 'expenses'

    expense_id = Column(Integer, primary_key=True)
    amount = Column(DECIMAL(10, 2), nullable=False)
    description = Column(Text)
    date = Column(Date, default=datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.group_id', ondelete='SET NULL'))
    category_id = Column(Integer, ForeignKey('categories.category_id', ondelete='SET NULL'))

    user = relationship('User', back_populates='expenses')
    group = relationship('Group', back_populates='expenses')
    category = relationship('Category', back_populates='expenses')

def init_db():
    """Create models"""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()