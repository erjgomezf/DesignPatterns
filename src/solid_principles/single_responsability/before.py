import os
from dataclasses import dataclass

import stripe
from dotenv import load_dotenv
from stripe import Charge
from stripe.error import StripeError

_ = load_dotenv()

@dataclass
class PaymentProcessor:
    def process_transaction(self, customer_data, payment_data) -> Charge:
        if not customer_data.get("name"):
            print("datos del cliente invalidos: hay que enviar un nombre")
            raise ValueError("Invalid customer data: missing name")
        
        if not customer_data.get("contact_info"):
            print("datos del cliente invalidos: hay que enviar un email o telefono")
            raise ValueError("Invalid customer data: missing contact info")
        
        if not payment_data.get("source"):
            print("datos de pago invalidos")
            raise ValueError("Invalid payment data")
        
        stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
        
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
            return charge
        
        with open("transaction_log.txt", "a") as log_file:
            log_file.write(f"{customer_data['name']} - paid {payment_data['amount']} - {charge.id}\n")
            log_file.write(f"Payment status: {charge.status}\n")
            
        return charge
    
if __name__ == "__main__":
    payment_processor = PaymentProcessor()
    
    customer_data_with_email = {
        "name": "John Doe",
        "contact_info": {"email": "e@gmail.com"},
    }
    
    customer_data_with_phone = {
        "name": "Jane Smith",
        "contact_info": {"phone": "+1234567890"},
    }
    
    payment_data = {
        "amount": 1000,
        "source": "tok_visa",
        "cvv": "123"
        }
    
    payment_processor.process_transaction(customer_data_with_email, payment_data)
    payment_processor.process_transaction(customer_data_with_phone, payment_data)