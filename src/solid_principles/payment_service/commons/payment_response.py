from typing import Optional #Para definir interfaces y tipos de datos opcionales.
from pydantic import BaseModel #Para validaciones de datos y creación de modelos de datos.


class PaymentResponse(BaseModel):
    status: str
    amount: int
    transaction_id: Optional[str] = None
    message: Optional[str] = None
