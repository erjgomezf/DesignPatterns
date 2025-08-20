import os
from dataclasses import dataclass

import stripe

from dotenv import load_dotenv
from stripe import Charge
from stripe.error import StripeError

_ = load_dotenv()

@dataclass
class CustomerValidator:
    def validate(self, customer_data):      
        if not customer_data.get("name"):
            print("datos del cliente invalidos: hay que enviar un nombre")
            raise ValueError("Invalid customer data: missing name")
        
        if not customer_data.get("contact_info"):
            print("datos del cliente invalidos: hay que enviar un email o telefono")
            raise ValueError("Invalid customer data: missing contact info")
        
@dataclass
class PaymentDataValidator:
    def validate (self, payment_data):
        if not payment_data.get("source"):
            print("datos de pago invalidos")
            raise ValueError("Invalid payment data")
        
@dataclass
class Notifier:
    def send_confirmation(self, customer_data):
        if "email" in customer_data["contact_info"]:
            # import smtplib
            from email.mime.text import MIMEText
            
            msg = MIMEText("Gracias por su compra.")
            msg["Subject"] = "Confirmación de compra"
            msg["From"] = "no-reply@example.com"
            msg["To"] = customer_data["contact_info"]["email"]
            
            # server = smtplib.SMTP("localhost")
            # server.send_message(msg)
            # server.quit()
            print(f"Email enviado a {customer_data['contact_info']['email']}")
            
        elif "phone" in customer_data["contact_info"]:
            phone_number = customer_data["contact_info"]["phone"]
            sms_gateway = "La puerta de enlace para enviar SMS"
            print(
                f"SMS enviado usando la puerta de enlace {sms_gateway} al número {phone_number}: Gracias por su compra."
            )
            
        else:
            print("No se pudo enviar la notificación: falta información de contacto")

@dataclass
class TransactionLogger:
    def log(self, customer_data, payment_data, charge):
        with open("transaction_log.txt", "a") as log_file:
            log_file.write(f"{customer_data['name']} - paid {payment_data['amount']} - {charge.id}\n")
            log_file.write(f"Payment status: {charge.status}\n")

@dataclass
class StripePaymentProcessor:
    def process_transaction(self, customer_data, payment_data) -> Charge:
        stripe.api_key = os.getenv("STRIPE_API_KEY")
        
        try:
            charge = stripe.Charge.create(
                amount=payment_data["amount"],
                currency="usd",
                source=payment_data["source"],
                description="Cargo por " + customer_data["name"],
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
    payment_processor = StripePaymentProcessor()
    notifier = Notifier()
    logger = TransactionLogger()
    
    def process_transaction(self, customer_data, payment_data) -> Charge:
        
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
    payment_processor = PaymentService()
    
    customer_data_with_email = {
        "name": "John Smith",
        "contact_info": {"email": "Smith@gmail.com"},
    }
    
    customer_data_with_phone = {
        "name": "Jane Smith",
        "contact_info": {"phone": "+1234567890"},
    }
    
    #payment_data = {"amount" : 15000, "source" : "tok_visa" , "cvv" : 123}

    #payment_processor.process_transaction(customer_data_with_email, payment_data)
    #payment_processor.process_transaction(customer_data_with_phone, payment_data)
    
    payment_data = {"amount" : 2000, "source" : "tok_radarBlock" , "cvv" : 123}
    
    try:
        payment_processor.process_transaction(customer_data_with_phone, payment_data)
    except ValueError as e:
        print(f"Error de validación: {e}")
    