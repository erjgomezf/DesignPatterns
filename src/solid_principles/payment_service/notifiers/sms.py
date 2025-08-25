from ..commons import CustomerData
from .notifier import NotifierProtocol

from dataclasses import dataclass


@dataclass
class SMSNotifier(NotifierProtocol):
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