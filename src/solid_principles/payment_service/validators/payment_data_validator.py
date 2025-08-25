from ..commons import PaymentData


class PaymentDataValidator:
    """
    Validador de datos de pago.
    """
    def validate(self, payment_data: PaymentData):
        """
        Valida los datos de pago.
        :param payment_data: Datos del pago que incluyen monto y fuente de pago.
        :type payment_data: PaymentData
        :raises ValueError: Si los datos de pago son inválidos, como falta de fuente o monto no positivo.
        """
        if not payment_data.source:
            print("datos de pago invalidos, falta información de fuente")
            raise ValueError("Invalid payment data: missing source")
        if payment_data.amount <= 0:
            print("datos de pago invalidos, el monto debe ser mayor a cero")
            raise ValueError("Invalid payment data: amount must be positive")