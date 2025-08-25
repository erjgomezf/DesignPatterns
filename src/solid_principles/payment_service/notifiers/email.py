from ..commons import CustomerData
from .notifier import NotifierProtocol

class EmailNotifier(NotifierProtocol):
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