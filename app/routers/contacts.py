from fastapi import APIRouter, Depends
from data_interactor import get_all, create_contact, update_contact, del_contact
from models import ContactCreate

router = APIRouter()

@router.get('/')
def get_all_contacts():
    return get_all()

@router.post('/')
def add_contact(contact: ContactCreate):
    id = create_contact(contact)
    return {'message': 'success', 'id': id}

@router.put('/{id}')
def change_contact(id: int, updated_contact: ContactCreate):
    update_contact(id, updated_contact)
    return {'message': 'success'}

@router.delete('/{id}')
def delete_contact(id: int):
    del_contact(id)
    return {'message': 'success'}