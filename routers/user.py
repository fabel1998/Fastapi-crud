from fastapi import APIRouter, Depends,Response
from sqlalchemy.orm import Session

from databases import get_db
from schemas import User, ShowUser
from repository import user

router = APIRouter(prefix='/user', tags=['users'])


@router.post('/', response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=ShowUser)
def get_user(id, response: Response, db: Session = Depends(get_db)):
    return user.show(id, db)
