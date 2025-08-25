from pydantic import BaseModel #Para validaciones de datos y creación de modelos de datos.


class PaymentData(BaseModel):
    amount: int
    source: str
    currency: str = "USD"