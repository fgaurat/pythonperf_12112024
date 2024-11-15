
from pydantic import BaseModel
class User(BaseModel):
    id:int
    name:str
    is_active:bool=True

def main():
    u = User(id=1,name="MARTIN")
    u1 = User(id=1,name="MARTIN")
    print(u==u1
          )
if __name__=='__main__':
    main()
