from typing import Protocol
from ..commons import CustomerData

class NotifierProtocol(Protocol):
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
