from .concrete_processors import CSVDataProcessor, APIDataProcessor

def client_code(data_processor):
    """
    El código cliente trabaja con la clase abstracta a través de su interfaz.
    """
    data_processor.process()

if __name__ == "__main__":
    print("Procesando datos de un CSV:")
    csv_processor = CSVDataProcessor()
    client_code(csv_processor)

    print("\n" + "="*30 + "\n")

    print("Procesando datos de una API:")
    api_processor = APIDataProcessor()
    client_code(api_processor)
