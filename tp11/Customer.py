from pydantic import BaseModel


class Customer(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    gender:str
    ip_address:str
