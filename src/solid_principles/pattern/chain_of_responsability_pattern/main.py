from .handlers import ManagerApprovalHandler, DirectorApprovalHandler, CEOApprovalHandler
from .request import PurchaseRequest


def client_code(handler: ManagerApprovalHandler, request: PurchaseRequest) -> None:
    """
    El código cliente envía una solicitud al primer manejador de la cadena.
    """
    print(f"\nCliente: Enviando solicitud {request.id} con monto ${request.amount}...")
    result = handler.handle(request)

    if result:
        print(f"  {result}")
    else:
        print(f"  Solicitud {request.id}: No pudo ser manejada por ningún miembro de la cadena.")


def main():
    """
    Función principal que demuestra el patrón Chain of Responsibility.
    """
    print("--- Demostración del Patrón de Diseño Chain of Responsibility ---\n")

    # 1. Configurar la cadena de responsabilidad.
    # El orden es importante: Gerente -> Director -> CEO
    manager = ManagerApprovalHandler()
    director = DirectorApprovalHandler()
    ceo = CEOApprovalHandler()

    manager.set_next(director).set_next(ceo)

    # 2. Crear y enviar diferentes solicitudes de compra.
    requests = [
        PurchaseRequest(id=1, amount=500),    # Aprobado por Gerente
        PurchaseRequest(id=2, amount=2500),   # Aprobado por Director
        PurchaseRequest(id=3, amount=10000),  # Aprobado por CEO
        PurchaseRequest(id=4, amount=999),    # Aprobado por Gerente
    ]

    for req in requests:
        client_code(manager, req)

    print("\n--- Fin de la demostración ---")


if __name__ == "__main__":
    main()