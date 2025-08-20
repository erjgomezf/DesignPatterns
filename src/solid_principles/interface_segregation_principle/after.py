import os
from dataclasses import dataclass, field #Para simplificar la creación de clases que son principalmente contenedores de datos.
from typing import Optional, Protocol # Para indicar que un valor puede ser de un tipo específico o None.

import stripe
from dotenv import load_dotenv #Para cargar variables de entorno desde un archivo .env.
from pydantic import BaseModel #Libreria mas utilizada para validaciones de datos.
from stripe import Charge
from stripe.error import StripeError

_ = load_dotenv()

class ContactInfo(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None

class CustomerData(BaseModel):
    name: str
    contact_info: ContactInfo
    
class PaymentData(BaseModel):
    amount: int
    source: str
    cvv: Optional[int] = None

@dataclass
class CustomerValidator:
    def validate(self, customer_data: CustomerData):      
        if not customer_data.name:
            print("datos del cliente invalidos: hay que enviar un nombre")
            raise ValueError("Invalid customer data: missing name")    
        if not customer_data.contact_info:
            print("datos del cliente invalidos: falta información de contacto")
            raise ValueError("Invalid customer data: missing contact info")
        if not (customer_data.contact_info.email or customer_data.contact_info.phone):
            print("datos del cliente invalidos: hay que enviar un email o telefono")
            raise ValueError("Invalid customer data: missing email or phone")
        
@dataclass
class PaymentDataValidator:
    def validate (self, payment_data:PaymentData):
        if not payment_data.source:
            print("datos de pago invalidos, falta información de fuente")
            raise ValueError("Invalid payment data: missing source")
        if payment_data.amount <= 0:
            print("datos de pago invalidos, el monto debe ser mayor a cero")
            raise ValueError("Invalid payment data: amount must be greater than zero")

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


class EmailNotifier(Notifier):
    def send_confirmation(self, customer_data: CustomerData):
        from email.mime.text import MIMEText
        
        msg = MIMEText("Gracias por su compra.")
        msg["Subject"] = "Confirmación de compra"
        msg["From"] = "no-reply@example.com"
        msg["To"] = customer_data.contact_info.email or ""
            
        print(f"Email enviado a {customer_data.contact_info.email}")

@dataclass
class SMSNotifier(Notifier):
    def send_confirmation(self, customer_data: CustomerData):
        phone_number = customer_data.contact_info.phone
        sms_gateway = "La puerta de enlace para enviar SMS"
        print(f"SMS enviado usando la puerta de enlace {sms_gateway} al número {phone_number}: Gracias por su compra.")            
        
@dataclass
class TransactionLogger:
    def log(self, customer_data: CustomerData, payment_data:PaymentData, charge: Charge):
        with open("transaction_log.txt", "a") as log_file:
            log_file.write(f"{customer_data.name} - paid {payment_data.amount} - {charge.id}\n")
            log_file.write(f"Payment status: {charge['status']}\n")

class PaymentProcessor(Protocol):
    """
    Protocolo para procesar transacciones de pago.
    
    Este protocolo define la interfaz que cualquier clase de procesamiento de pagos debe implementar.
    La implementacion deberá proporcionar un método 'process_transaction' que procese una transacción de pago y retorne un objeto Charge.
    """
    def process_transaction(self, customer_data: CustomerData, payment_data:PaymentData) -> Charge:
        """
        Procesa una transacción de pago.
        :param customer_data: Datos del cliente que incluyen información de contacto.
        :type customer_data: CustomerData
        :param payment_data: Datos del pago que incluyen monto y fuente.
        :type payment_data: PaymentData
        :return: Un objeto Charge que representa el resultado de la transacción.
        :rtype: Charge
        """
        ...
@dataclass
class StripePaymentProcessor(PaymentProcessor):
    def process_transaction(self, customer_data: CustomerData, payment_data:PaymentData) -> Charge:
        stripe.api_key = os.getenv("STRIPE_API_KEY")
        
        try:
            charge = stripe.Charge.create(
                amount=payment_data.amount,
                currency="usd",
                source=payment_data.source,
                description="Cargo por " + customer_data.name,
            )
            print("Transacción exitosa:")
            
        except StripeError as e:
            print("Error procesando la transacción:", e)
            raise e
    
        return charge


@dataclass
class PaymentService:
    customer_validator = CustomerValidator()
    payment_validator = PaymentDataValidator()
    payment_processor : PaymentProcessor = field(default_factory=StripePaymentProcessor)
    notifier : Notifier = field(default_factory=EmailNotifier)
    #notifier : Notifier = field(default_factory=SMSNotifier())
    logger = TransactionLogger()
    
    def process_transaction(self, customer_data: CustomerData, payment_data:PaymentData) -> Charge:
        
        try:
            self.customer_validator.validate(customer_data)
        except ValueError as e:
            raise e
        
        try: 
            self.payment_validator.validate(payment_data)
        except ValueError as e:
            raise e
        
        try:
            charge = self.payment_processor.process_transaction(customer_data, payment_data)
            self.notifier.send_confirmation(customer_data)
            self.logger.log(customer_data, payment_data, charge)
            return charge
        except StripeError as e:
            print("Error al procesar la transacción")
            raise e

    
if __name__ == "__main__":
    sms_notifier = SMSNotifier()
    payment_processor = PaymentService(notifier=sms_notifier)
    
    customer_data_with_email = CustomerData(
        name= "John Smith",
        contact_info = ContactInfo(email="Smith@gmail.com")
    )
    
    customer_data_with_phone = CustomerData(
        name= "Jane Smith",
        contact_info = ContactInfo(phone="+1234567890")
    )
    
    #payment_data = {"amount" : 15000, "source" : "tok_visa" , "cvv" : 123}

    #payment_processor.process_transaction(customer_data_with_email, payment_data)
    #payment_processor.process_transaction(customer_data_with_phone, payment_data)
    
    #payment_data = {"amount" : 2000, "source" : "tok_visa" , "cvv" : 123}
    payment_data = PaymentData(amount=2000, source="tok_visa", cvv=123)
    
    try:
        payment_processor.process_transaction(customer_data_with_phone, payment_data)
    except ValueError as e:
        print(f"Error de validación: {e}")