from typing import Optional
from pydantic import BaseModel

class vh(BaseModel):
    name_product: str
    price: Optional[int]
    stock: Optional[int]
    category_id: Optional[int] 
    modelo_id: Optional[int] 
    class Config:
      from_attributes = True
      


    


    
    
