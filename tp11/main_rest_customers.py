from Customer import Customer
from CustomerDAO import CustomerDAO
from fastapi import FastAPI
from typing import List
app = FastAPI()

@app.get("/customers", response_model=List[Customer])
def get_customers():
    with CustomerDAO("../customers_db.db") as dao:
        customers = list(dao.find_all())  
    return customers