from fastapi import APIRouter, Depends, status, Response
from typing import List
from sqlalchemy.orm import Session

from databases import get_db
from schemas import Blog, ShowBlog, User
from repository import blog
from oauth_2 import get_current_user

router = APIRouter(
	prefix = '/blog',
	tags = ['blogs']
)

@router.get('/', response_model=List[ShowBlog])
def all(db : Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	
	return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db : Session = Depends(get_db)):
	
	return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db : Session = Depends(get_db)):
	
	return blog.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Blog,  db : Session = Depends(get_db)):
	
	return blog.update(id, request, db)



@router.get('/{id}', status_code=200, response_model=ShowBlog)
def show(id, response: Response, db : Session = Depends(get_db)):
	
	return blog.show(id, db)
	
