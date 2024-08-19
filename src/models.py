import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(30), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password =Column(String(45), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, primary_key=True)
    post_text = Column(String(250), nullable=False)
    post_picture = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(User)

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.user_id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    
    user_from = relationship(User, foreign_keys=[user_from_id])
    user_to = relationship(User, foreign_keys=[user_to_id])

class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    post_id =  Column(Integer, ForeignKey('post.post_id'), nullable=False)
    post = relationship(Post)
    author_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    type = Column(String(50))
    url = Column(String(2048))
    post_id =  Column(Integer, ForeignKey('post.post_id'), nullable=False)
    post = relationship(Post)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e


