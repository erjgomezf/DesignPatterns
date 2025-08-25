from ..commons import CustomerData


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