from typing import Optional #Para definir interfaces y tipos de datos opcionales.
from pydantic import BaseModel #Para validaciones de datos y creación de modelos de datos.

from .contact import ContactInfo

class CustomerData(BaseModel):
    name: str
    contact_info: ContactInfo
    customer_id: Optional[str] = None