from fastapi import APIRouter, Depends
from data_interactor import DAL
from models import ContactCreate

router = APIRouter()

dal = DAL()

@router.get('/')
def get_all_contacts():
    return dal.get_all()

@router.post('/')
def add_contact(contact: ContactCreate):
    id = dal.create_contact(contact)
    return {'message': 'success', 'id': id}

@router.put('/{id}')
def change_contact(id: int, updated_contact: ContactCreate):
    dal.update_contact(id, updated_contact)
    return {'message': 'success'}

@router.delete('/{id}')
def delete_contact(id: int):
    dal.del_contact(id)
    return {'message': 'success'}