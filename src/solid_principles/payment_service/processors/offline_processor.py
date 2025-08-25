from ..commons import CustomerData, PaymentData, PaymentResponse
from ..processors import PaymentProcessorProtocol
import uuid


class OfflinePaymentProcessor(PaymentProcessorProtocol):
    def process_transaction(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse:
        """
        Procesador de pagos offline.
        :param customer_data: Datos del cliente que incluyen nombre y contacto.
        :type customer_data: CustomerData
        :param payment_data: Datos del pago que incluyen monto y fuente de pago.
        :type payment_data: PaymentData
        :return: Un objeto PaymentResponse que contiene el estado de la transacción, el monto, el ID de la transacción y un mensaje.
        :rtype: PaymentResponse
        """
        print("Procesando pago offline para", customer_data.name)
        return PaymentResponse(
            status="success",
            amount=payment_data.amount,
            transaction_id=str(uuid.uuid4()),
            message="pago offline exitoso",
        )
   