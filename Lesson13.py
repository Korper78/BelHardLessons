"""
Описание Alchemy.ORM-моделей DB-домашки
"""

from datetime import datetime
from sqlalchemy import Column, BigInteger, VARCHAR, TEXT, ForeignKey, TIMESTAMP, BOOLEAN
from sqlalchemy.orm import declarative_base

HWBase = declarative_base()


class User(HWBase):
    __tablename__: str = 'users'
    id = Column(BigInteger, primary_key=True)
    email = Column(VARCHAR(255))
    password = Column(VARCHAR(64))
    name = Column(VARCHAR(255), nullable=False)
    time_registration = Column(TIMESTAMP, default=datetime.now().timestamp())


class Role(HWBase):
    __tablename__: str = 'roles'
    id = Column(BigInteger, primary_key=True)
    role = Column(VARCHAR(255), nullable=False, unique=True)


class Tag(HWBase):
    __tablename__: str = 'tags'
    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(50), nullable=False)


class Dialog(HWBase):
    __tablename__: str = 'dialogs'
    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    time_creation = Column(TIMESTAMP, default=datetime.now().timestamp())


class Friends(HWBase):
    __tablename__: str = 'friends'
    friend1_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'))
    friend2_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'))
    time_creation = Column(TIMESTAMP, default=datetime.now().timestamp())


class UserToRole(HWBase):
    __tablename__: str = 'users_to_roles'
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    role_id = Column(BigInteger, ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)


class Album(HWBase):
    __tablename__: str = 'albums'
    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'))
    time_creation = Column(TIMESTAMP, default=datetime.now().timestamp())


class UserToDialog(HWBase):
    __tablename__: str = 'users_to_dialogs'
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'))
    dialog_id = Column(BigInteger, ForeignKey('dialogs.id', ondelete='CASCADE'))
    time_creation = Column(TIMESTAMP, default=datetime.now().timestamp())


class Photo(HWBase):
    __tablename__: str = 'photos'
    id = Column(BigInteger, primary_key=True)
    path = Column(VARCHAR(255), nullable=False)
    description = Column(VARCHAR(255))
    album_id = Column(BigInteger, ForeignKey('albums.id', ondelete='CASCADE'))
    time_creation = Column(TIMESTAMP, default=datetime.now().timestamp())


class TagToPhoto(HWBase):
    __tablename__: str = 'tags_to_photos'
    photo_id = Column(BigInteger, ForeignKey('photos.id', ondelete='CASCADE'), nullable=False)
    tag_id = Column(BigInteger, ForeignKey('tags.id', ondelete='CASCADE'), nullable=False)


class Message(HWBase):
    __tablename__: str = 'messages'
    id = Column(BigInteger, primary_key=True)
    dialog_id = Column(BigInteger, ForeignKey('dialogs.id', ondelete='CASCADE'))
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete='CASCADE'))
    text = Column(TEXT)
    time_creation = Column(TIMESTAMP, default=datetime.now().timestamp())
    text_changed = Column(BOOLEAN, default=False)


class MessageToPhoto(HWBase):
    __tablename__: str = 'messages_to_photos'
    photo_id = Column(BigInteger, ForeignKey('photos.id', ondelete='CASCADE'), nullable=False)
    message_id = Column(BigInteger, ForeignKey('messages.id', ondelete='CASCADE'), nullable=False)
