import os #Para acceder a las variables de entorno.
from dataclasses import dataclass, field #Para simplificar la creación de clases que son principalmente contenedores de datos.
from typing import Optional, Protocol #Para definir interfaces y tipos de datos opcionales.
import uuid #Para generar identificadores únicos universales (UUIDs).
import stripe #Para interactuar con la API de Stripe, una plataforma de pagos en línea.
from dotenv import load_dotenv #Para cargar variables de entorno desde un archivo .env.
from pydantic import BaseModel #Para validaciones de datos y creación de modelos de datos.
from stripe.error import StripeError #Para manejar errores específicos de Stripe.


_ = load_dotenv()


class ContactInfo(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None


class CustomerData(BaseModel):
    name: str
    contact_info: ContactInfo
    customer_id: Optional[str] = None


class PaymentData(BaseModel):
    amount: int
    source: str


class PaymentResponse(BaseModel):
    status: str
    amount: int
    transaction_id: Optional[str] = None
    message: Optional[str] = None


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
   

class Notifier(Protocol):
    """
    Protocolo para notificar al cliente sobre el estado de la transacción.
    
    Este protocolo define la interfaz que cualquier clase de notificación debe implementar.
    La implementacion deberá proporcional un metodo 'send_confirmation' que envíe una notificación al cliente.
    
    """
    def send_confirmation(self, customer_data: CustomerData): 
        """
        Envía una notificación de confirmación al cliente.
        
        :param customer_data: Datos del cliente que incluyen información de contacto.
        :tyoep customer_data: CustomerData
        """
        ...


class EmailNotifier:
    def send_confirmation(self, customer_data: CustomerData):
        from email.mime.text import MIMEText
        """
        Envía una notificación de confirmación por correo electrónico al cliente.
        :param customer_data: Datos del cliente que incluyen información de contacto.
        :type customer_data: CustomerData
        :raises ValueError: Si el cliente no tiene una dirección de correo electrónico.
        """

        if not customer_data.contact_info.email:
            raise ValueError("Email address is requiered to send an email")

        msg = MIMEText("Gracias por su compra.")
        msg["Subject"] = "Confirmación de compra"
        msg["From"] = "no-reply@example.com"
        msg["To"] = customer_data.contact_info.email or ""

        print(f"Email enviado a {customer_data.contact_info.email}")


@dataclass
class SMSNotifier:
    gateway: str
    """
    Notificador de SMS que envía mensajes de confirmación al cliente.
    :param gateway: El servicio de puerta de enlace SMS utilizado para enviar mensajes.
    :type gateway: str
    """
    def send_confirmation(self, customer_data: CustomerData):
        """
        Envía una notificación de confirmación por SMS al cliente.
        :param customer_data: Datos del cliente que incluyen información de contacto.
        :type customer_data: CustomerData
        """
        phone_number = customer_data.contact_info.phone
        if not phone_number:
            print("datos del cliente invalidos: falta información de contacto")
            return
        print(
            f"SMS enviado usando la puerta de enlace {self.gateway} al número {phone_number}: Gracias por su compra."
        )


class TransactionLogger:
    """
    Clase para registrar transacciones y reembolsos en un archivo de registro.
    Esta clase proporciona métodos para registrar transacciones y reembolsos en un archivo de texto.
    """
    def log_transaction(
        self,
        customer_data: CustomerData,
        payment_data: PaymentData,
        payment_response: PaymentResponse,
    ):
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

    def log_refund(
        self, transaction_id: str, refund_response: PaymentResponse
    ):
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


class CustomerValidator:
    """
    Validador de datos del cliente.
    """
    def validate(self, customer_data: CustomerData):
        """
        Valida los datos del cliente.
        :param customer_data: Datos del cliente que incluyen nombre y contacto.
        :type customer_data: CustomerData
        :raises ValueError: Si los datos del cliente son inválidos, como falta de nombre o información de contacto.
        """
        if not customer_data.name:
            print("datos del cliente invalidos: hay que enviar un nombre")
            raise ValueError("Invalid customer data: missing name")
        if not customer_data.contact_info:
            print("datos del cliente invalidos: falta información de contacto")
            raise ValueError("Invalid customer data: missing contact info")
        if not (customer_data.contact_info.email or customer_data.contact_info.phone):
            print("datos del cliente invalidos: hay que enviar un email o telefono")
            raise ValueError("Invalid customer data: missing email and phone")


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


@dataclass
class PaymentService:
    """
    Servicio de procesamiento de pagos que utiliza un procesador de pagos, un notificador y validadores de datos.
    Este servicio permite procesar transacciones de pago, reembolsos y pagos recurrentes.
    """
    payment_processor: PaymentProcessorProtocol
    notifier: Notifier
    customer_validator: CustomerValidator = field(default_factory=CustomerValidator)
    payment_validator: PaymentDataValidator = field(default_factory=PaymentDataValidator)
    logger: TransactionLogger = field(default_factory=TransactionLogger)
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


if __name__ == "__main__":
    # Levantar el procesador de pagos de Stripe y el procesador de pagos offline
    stripe_processor = StripePaymentProcessor()
    offline_processor = OfflinePaymentProcessor()

    # Levanta los datos del cliente
    customer_data_with_email = CustomerData(
        name="John Doe", contact_info=ContactInfo(email="john@example.com")
    )
    customer_data_with_phone = CustomerData(
        name="Jane Doe", contact_info=ContactInfo(phone="1234567890")
    )

    # Levanta los datos de pago
    payment_data = PaymentData(amount=100, source="tok_visa")

    # Levanta los notifiers
    email_notifier = EmailNotifier()

    sms_gateway = "Tu puerta de enlace SMS"
    sms_notifier = SMSNotifier(sms_gateway)

    # Usando el procesador de pagos de Stripe con el notificador de correo electrónico
    payment_service_email = PaymentService(stripe_processor, email_notifier, recurring_processor = stripe_processor, refund_processor = stripe_processor) 
    payment_service_email.process_transaction(customer_data_with_email, payment_data)

    # Usando el procesador de pagos de Stripe con el notificador de SMS
    payment_service_sms = PaymentService(stripe_processor, sms_notifier)
    sms_payment_response = payment_service_sms.process_transaction(customer_data_with_phone, payment_data)

    # Ejemplo de reembolso usando el procesador de pagos de Stripe
    transaction_id_to_refund = sms_payment_response.transaction_id
    if transaction_id_to_refund:
        payment_service_email.process_refund(transaction_id_to_refund)

    # Usando el procesador de pagos offline con el notificador de correo electrónico
    offline_payment_service = PaymentService(offline_processor, email_notifier)
    offline_payment_response = offline_payment_service.process_transaction(customer_data_with_email, payment_data)

    # Hace un intento de reembolso usando el procesador offline (fallará)
    try:
        if offline_payment_response.transaction_id:
            offline_payment_service.process_refund(offline_payment_response.transaction_id)
    except Exception as e:
        print(f"Refund failed and PaymentService raised an exception: {e}")

    
    # Hace un intento de configurar un pago recurrente usando el procesador offline (fallará)
    try:
        offline_payment_service.setup_recurring(customer_data_with_email, payment_data)

    except Exception as e:
        print(f"Recurring payment setup failed and PaymentService raised an exception {e}")

    try:
        error_payment_data = PaymentData(amount=100, source="tok_radarBlock")
        payment_service_email.process_transaction(customer_data_with_email, error_payment_data)
    except Exception as e:
        print(f"Payment failed and PaymentService raised an exception: {e}")

    # Levanta los datos de pago recurrente
    recurring_payment_data = PaymentData(amount=100, source="pm_card_visa")
    payment_service_email.setup_recurring(customer_data_with_email, recurring_payment_data)