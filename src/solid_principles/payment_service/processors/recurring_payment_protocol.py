from ..commons import CustomerData, PaymentData, PaymentResponse
from typing import Protocol


class RecurringPaymentProtocol(Protocol):
    """
    Protocolo para procesar pagos recurrentes.
    
    Este protocolo define la interfaz que cualquier clase de procesamiento de pagos recurrentes debe implementar.
    La implementacion deberá proporcionar un método 'setup_recurring_payment' que configure un pago recurrente y retorne un objeto PaymentResponse.
    """
    
    def setup_recurring_payment(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse:
        """
        Configura un pago recurrente y retorna un objeto PaymentResponse.
        :param customer_data: Datos del cliente.
        :param payment_data: Datos del pago.
        :return: Un objeto PaymentResponse que contiene el estado del pago recurrente, el monto, el ID de la transacción y un mensaje.
        :rtype: PaymentResponse
        """
        ...