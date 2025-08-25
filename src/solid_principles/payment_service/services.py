from .commons import CustomerData, PaymentData, PaymentResponse
from .loggers import TransactionLogger
from .notifiers import NotifierProtocol
from .processors import PaymentProcessorProtocol, RefundPaymentProtocol, RecurringPaymentProtocol
from .validators import CustomerValidator, PaymentDataValidator

from dataclasses import dataclass
from typing import Optional


@dataclass
class PaymentService:
    """
    Servicio de procesamiento de pagos que utiliza un procesador de pagos, un notificador y validadores de datos.
    Este servicio permite procesar transacciones de pago, reembolsos y pagos recurrentes.
    """
    payment_processor: PaymentProcessorProtocol
    notifier: NotifierProtocol
    customer_validator: CustomerValidator
    payment_validator: PaymentDataValidator
    logger: TransactionLogger
    recurring_processor: Optional[RecurringPaymentProtocol] = None
    refund_processor: Optional[RefundPaymentProtocol] = None


    def process_transaction(self, customer_data: CustomerData, payment_data: PaymentData) -> PaymentResponse:
        """
        Procesa una transacción de pago utilizando el procesador de pagos.
        :param customer_data: Datos del cliente que incluyen nombre y contacto.
        :type customer_data: CustomerData
        :param payment_data: Datos del pago que incluyen monto y fuente de pago.
        :type payment_data: PaymentData
        :return: Un objeto PaymentResponse que contiene el estado de la transacción, el monto, el ID de la transacción y un mensaje.
        :rtype: PaymentResponse
        """
        self.customer_validator.validate(customer_data)
        self.payment_validator.validate(payment_data)
        payment_response = self.payment_processor.process_transaction(
            customer_data, payment_data
        )
        self.notifier.send_confirmation(customer_data)
        self.logger.log_transaction(
            customer_data, payment_data, payment_response
        )
        return payment_response

    def process_refund(self, transaction_id: str):
        """
        Procesa un reembolso utilizando el procesador de reembolsos.
        :param transaction_id: ID de la transacción a reembolsar.
        :type transaction_id: str
        :return: Un objeto PaymentResponse que contiene el estado del reembolso, el monto, el ID de la transacción y un mensaje.
        :rtype: PaymentResponse
        """
        if not self.refund_processor:
            raise Exception("Este procesador no soporta reembolsos.")
        refund_response = self.refund_processor.refund_payment(transaction_id)
        self.logger.log_refund(transaction_id, refund_response)
        return refund_response

    def setup_recurring(self, customer_data: CustomerData, payment_data: PaymentData):
        """
        Configura un pago recurrente utilizando el procesador de pagos recurrentes.
        :param customer_data: Datos del cliente que incluyen nombre y contacto.
        :type customer_data: CustomerData
        :param payment_data: Datos del pago que incluyen monto y fuente de pago.
        :type payment_data: PaymentData
        :return: Un objeto PaymentResponse que contiene el estado del pago recurrente, el monto, el ID de la transacción y un mensaje.
        :rtype: PaymentResponse
        """
        if not self.recurring_processor:
            raise Exception("Este procesador no soporta pagos recurrentes.")
        recurring_response = self.recurring_processor.setup_recurring_payment(
            customer_data, payment_data
        )
        self.logger.log_transaction(
            customer_data, payment_data, recurring_response
        )
        return recurring_response