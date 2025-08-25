from ..commons import CustomerData, PaymentData, PaymentResponse
from processors import PaymentProcessorProtocol, RefundPaymentProtocol, RecurringPaymentProtocol

import stripe, os
from stripe.error import StripeError

class StripePaymentProcessor(PaymentProcessorProtocol, RefundPaymentProtocol, RecurringPaymentProtocol):
    """
    Procesador de pagos que utiliza la API de Stripe para manejar transacciones, reembolsos y pagos recurrentes.
    Esta clase implementa los protocolos PaymentProcessor, RefundPaymentProcessor y RecurringPaymentProcessor.
    """
    
    def process_transaction(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse:
        """
        Procesa una transacción de pago utilizando la API de Stripe.
        :param customer_data: Datos del cliente que incluyen nombre y contacto.
        :type customer_data: CustomerData
        :param payment_data: Datos del pago que incluyen monto y fuente de pago.
        :type payment_data: PaymentData
        :return: Un objeto PaymentResponse que contiene el estado de la transacción, el monto, el ID de la transacción y un mensaje.
        :rtype: PaymentResponse
        """
        stripe.api_key = os.getenv("STRIPE_API_KEY")
        try:
            charge = stripe.Charge.create(
                amount=payment_data.amount,
                currency="usd",
                source=payment_data.source,
                description="Cargo por " + customer_data.name,
            )
            print("Transacción exitosa:")
            return PaymentResponse(
                status=charge["status"],
                amount=charge["amount"],
                transaction_id=charge["id"],
                message="Transacción exitosa",
            )
        except StripeError as e:
            print("Error procesando la transacción:", e)
            return PaymentResponse(
                status="failed",
                amount=payment_data.amount,
                transaction_id=None,
                message=str(e),
            )

    def refund_payment(self, transaction_id: str) -> PaymentResponse:
        """
        Reembolso un pago utilizando la API de Stripe.
        :param transaction_id: ID de la transacción a reembolsar.
        :type transaction_id: str
        :return: Un objeto PaymentResponse que contiene el estado del reembolso, el monto, el ID de la transacción y un mensaje.
        :rtype: PaymentResponse
        """
        stripe.api_key = os.getenv("STRIPE_API_KEY")
        try:
            refund = stripe.Refund.create(charge=transaction_id)
            print("Reembolso exitoso:")
            return PaymentResponse(
                status=refund["status"],
                amount=refund["amount"],
                transaction_id=refund["id"],
                message="Reembolso exitoso",
            )
        except StripeError as e:
            print("Error procesando el reembolso:", e)
            return PaymentResponse(
                status="failed",
                amount=0,
                transaction_id=None,
                message=str(e),
            )

    def setup_recurring_payment(
        self, customer_data: CustomerData, payment_data: PaymentData
    ) -> PaymentResponse:
        """
        Configura un pago recurrente utilizando la API de Stripe.
        :param customer_data: Datos del cliente que incluyen nombre y contacto.
        :type customer_data: CustomerData
        :param payment_data: Datos del pago que incluyen monto y fuente de pago.
        :type payment_data: PaymentData
        :return: Un objeto PaymentResponse que contiene el estado del pago recurrente, el monto, el ID de la transacción y un mensaje.
        :rtype: PaymentResponse
        """
        stripe.api_key = os.getenv("STRIPE_API_KEY")
        price_id = os.getenv("STRIPE_PRICE_ID", "")
        try:
            customer = self._get_or_create_customer(customer_data)

            payment_method = self._attach_payment_method(
                customer.id, payment_data.source
            )

            self._set_default_payment_method(customer.id, payment_method.id)

            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[
                    {"price": price_id},
                ],
                expand=["latest_invoice.payment_intent"],
            )

            print("Configuración de pago recurrente exitosa:")
            amount = subscription["items"]["data"][0]["price"]["unit_amount"]
            return PaymentResponse(
                status=subscription["status"],
                amount=amount,
                transaction_id=subscription["id"],
                message="Configuración de pago recurrente exitosa",
            )
        except StripeError as e:
            print("Error configurando el pago recurrente:", e)
            return PaymentResponse(
                status="failed",
                amount=0,
                transaction_id=None,
                message=str(e),
            )

    def _get_or_create_customer(
        self, customer_data: CustomerData
    ) -> stripe.Customer:
        """
        Obtiene o crea un cliente en Stripe.
        :param customer_data: Datos del cliente que incluyen nombre y contacto.
        :type customer_data: CustomerData
        :return: Un objeto Customer de Stripe que representa al cliente.
        :rtype: stripe.Customer
        """
        if customer_data.customer_id:
            customer = stripe.Customer.retrieve(customer_data.customer_id)
            print(f"Cliente recuperado: {customer.id}")
        else:
            if not customer_data.contact_info.email:
                raise ValueError("Email is required to create a customer")
            customer = stripe.Customer.create(
                name=customer_data.name, email=customer_data.contact_info.email
            )
            print(f"Cliente creado: {customer.id}")
        return customer

    def _attach_payment_method(
        self, customer_id: str, payment_source: str
    ) -> stripe.PaymentMethod:
        """
        Adjunta un método de pago a un cliente en Stripe.
        :param customer_id: ID del cliente en Stripe.
        :type customer_id: str
        :param payment_source: Fuente de pago (como un token o ID de método de pago).
        :type payment_source: str
        :return: Un objeto PaymentMethod de Stripe que representa el método de pago adjunto.
        :rtype: stripe.PaymentMethod
        """
        payment_method = stripe.PaymentMethod.retrieve(payment_source)
        stripe.PaymentMethod.attach(
            payment_method.id,
            customer=customer_id,
        )
        print(
            f"Método de pago {payment_method.id} adjuntado al cliente {customer_id}"
        )
        return payment_method

    def _set_default_payment_method(
        self, customer_id: str, payment_method_id: str
    ) -> None:
        """
        Establece un método de pago predeterminado para un cliente en Stripe.
        :param customer_id: ID del cliente en Stripe.
        :type customer_id: str
        :param payment_method_id: ID del método de pago que se establecerá como predeterminado.
        :type payment_method_id: str
        :return: None
        :rtype: None
        """
        stripe.Customer.modify(
            customer_id,
            invoice_settings={
                "default_payment_method": payment_method_id,
            },
        )
        print(f"Método de pago predeterminado {payment_method_id} establecido para el cliente {customer_id}")