from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from schemas import User
from models import MyUser
from hashing import Hash


def create(request: User, db: Session):
	new_user = MyUser(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	
	return new_user

def show(id: int, db: Session):
	user = db.query(MyUser).filter(MyUser.id==id).first()
	if not user:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
	
	return user