from typing import Optional #Para definir interfaces y tipos de datos opcionales.
from pydantic import BaseModel #Para validaciones de datos y creación de modelos de datos.

class ContactInfo(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None