from databases import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class MyBlog(Base):

	__tablename__ = 'myblogs'

	id = Column(Integer, primary_key=True, index=True)
	title  = Column(String)
	body = Column(String)
	user_id = Column(Integer, ForeignKey('myusers.id'))
	creator = relationship('MyUser', back_populates='blogs')

class MyUser(Base):

	__tablename__ = 'myusers'

	id = Column(Integer, primary_key=True, index=True)
	name  = Column(String)
	email = Column(String)
	password = Column(String)
	blogs = relationship('MyBlog', back_populates='creator')
