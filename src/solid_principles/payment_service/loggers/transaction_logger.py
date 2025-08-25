from ..commons import CustomerData, PaymentData, PaymentResponse


class TransactionLogger:
    """
    Clase para registrar transacciones y reembolsos en un archivo de registro.
    Esta clase proporciona métodos para registrar transacciones y reembolsos en un archivo de texto.
    """
    def log_transaction(self,customer_data: CustomerData,payment_data: PaymentData,payment_response: PaymentResponse,):
        """
        Registra una transacción en un archivo de registro.
        :param customer_data: Datos del cliente que incluyen nombre y contacto.
        :type customer_data: CustomerData
        :param payment_data: Datos del pago que incluyen monto y fuente de pago.
        :type payment_data: PaymentData
        :param payment_response: Respuesta del procesamiento del pago que incluye estado, monto, ID de transacción y mensaje.
        :type payment_response: PaymentResponse
        """
        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"{customer_data.name} paid {payment_data.amount}\n"
            )
            log_file.write(f"Payment status: {payment_response.status}\n")
            if payment_response.transaction_id:
                log_file.write(
                    f"Transaction ID: {payment_response.transaction_id}\n"
                )
            log_file.write(f"Message: {payment_response.message}\n")

    def log_refund(self, transaction_id: str, refund_response: PaymentResponse):
        """
        Registra un reembolso en un archivo de registro.
        :param transaction_id: ID de la transacción a la que se le realiza el reembolso.
        :type transaction_id: str
        :param refund_response: Respuesta del procesamiento del reembolso que incluye estado, monto y mensaje.
        :type refund_response: PaymentResponse
        """
        with open("transactions.log", "a") as log_file:
            log_file.write(
                f"Refund processed for transaction {transaction_id}\n"
            )
            log_file.write(f"Refund status: {refund_response.status}\n")
            log_file.write(f"Message: {refund_response.message}\n")