from dataclasses import dataclass


@dataclass
class PurchaseRequest:
    """
    Representa una solicitud de compra que será procesada por la cadena.
    """
    id: int
    amount: float