from typing import Protocol
from ..commons import PaymentResponse


class RefundPaymentProtocol(Protocol):
    """
    Protocolo para procesar reembolsos de pagos.
    
    Este protocolo define la interfaz que cualquier clase de procesamiento de reembolsos debe implementar.
    La implementacion deberá proporcionar un método 'refund_payment' que procese un reembolso y retorne un objeto PaymentResponse.
    """
    
    def refund_payment(self, transaction_id: str) -> PaymentResponse:
        """
        Procesa un reembolso y retorna un objeto PaymentResponse.
        :param transaction_id: ID de la transacción a reembolsar.
        :return: Un objeto PaymentResponse que contiene el estado del reembolso, el monto, el ID de la transacción y un mensaje.
        :rtype: PaymentResponse
        """
        ...