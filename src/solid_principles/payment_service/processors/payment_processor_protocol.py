from ..commons import CustomerData, PaymentData, PaymentResponse
from typing import Protocol


class PaymentProcessorProtocol(Protocol): 
    """
    Protocolo para procesar transacciones de pago.
    
    Este protocolo define la interfaz que cualquier clase de procesamiento de pagos debe implementar.
    La implementacion deberá proporcionar un método 'process_transaction' que procese una transacción de pago y retorne un objeto Charge.
    """

    def process_transaction(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse: 
        """
        Procesa una transacción de pago y retorna un objeto PaymentResponse.
        :param customer_data: Datos del cliente.
        :param payment_data: Datos del pago.
        :return: Un objeto PaymentResponse que contiene el estado de la transacción, el monto, el ID de la transacción y un mensaje.
        :rtype: PaymentResponse
        """
        ...