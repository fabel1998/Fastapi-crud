from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from models import MyBlog
from schemas import Blog

def get_all(db: Session):
	blogs = db.query(MyBlog).all()
	
	return blogs

def create(request: Blog, db: Session):
	new_blog = MyBlog(title=request.title, body=request.body, user_id=1)
	db.add(new_blog)
	db.commit()
	db.refresh(new_blog)

	return new_blog

def destroy(id:int, db: Session):
	blog = db.query(MyBlog).filter(MyBlog.id==id)
	
	if not blog.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
	
	blog.delete(synchronize_session=False)
	db.commit()
	
	return 'done'

def update(id:int, db: Session, request: Blog,):
	blog = db.query(MyBlog).filter(MyBlog.id==id)
	
	if not blog.first():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
	
	blog.update(request)
	db.commit()
	
	return 'updated done'

def show(id:int, db: Session):
	blog = db.query(MyBlog).filter(MyBlog.id==id).first()
	
	if not blog:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
	
	return blog