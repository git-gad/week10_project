from pydantic import BaseModel

class ContactOutput(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_number: str
    
class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str