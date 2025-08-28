from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from .request import PurchaseRequest


class ApprovalHandler(ABC):
    """
    La interfaz Handler (Manejador) declara un método para construir la cadena
    de manejadores y un método para ejecutar una solicitud.
    """

    _next_handler: Optional[ApprovalHandler] = None

    def set_next(self, handler: ApprovalHandler) -> ApprovalHandler:
        """
        Establece el siguiente manejador en la cadena.
        Retorna el manejador pasado para facilitar el encadenamiento.
        """
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: PurchaseRequest) -> Optional[str]:
        """
        Procesa la solicitud o la pasa al siguiente manejador en la cadena.
        """
        if self._next_handler:
            return self._next_handler.handle(request)
        return None  # La solicitud no fue manejada por ningún manejador en la cadena


class ManagerApprovalHandler(ApprovalHandler):
    """
    Manejador Concreto: Aprueba solicitudes de hasta 1000.
    """

    def handle(self, request: PurchaseRequest) -> Optional[str]:
        if request.amount <= 1000:
            return f"Solicitud {request.id}: Aprobada por el Gerente (Monto: ${request.amount})"
        else:
            print(f"Solicitud {request.id}: Monto ${request.amount} demasiado alto para el Gerente. Pasando al siguiente...")
            return super().handle(request)


class DirectorApprovalHandler(ApprovalHandler):
    """
    Manejador Concreto: Aprueba solicitudes de hasta 5000.
    """

    def handle(self, request: PurchaseRequest) -> Optional[str]:
        if request.amount <= 5000:
            return f"Solicitud {request.id}: Aprobada por el Director (Monto: ${request.amount})"
        else:
            print(f"Solicitud {request.id}: Monto ${request.amount} demasiado alto para el Director. Pasando al siguiente...")
            return super().handle(request)


class CEOApprovalHandler(ApprovalHandler):
    """
    Manejador Concreto: Aprueba solicitudes de cualquier monto.
    """

    def handle(self, request: PurchaseRequest) -> Optional[str]:
        return f"Solicitud {request.id}: Aprobada por el CEO (Monto: ${request.amount})"