from .context import ReportGenerator
from .strategies import JsonExportStrategy, CsvExportStrategy, HtmlExportStrategy

def main():
    """
    Función principal que demuestra el patrón Strategy.
    """
    print("--- Demostración del Patrón de Diseño Strategy ---")

    # 1. Datos de ejemplo que queremos exportar.
    sample_data = [
        {"id": 1, "nombre": "Teclado Mecánico", "precio": 120},
        {"id": 2, "nombre": "Mouse RGB", "precio": 45},
        {"id": 3, "nombre": "Monitor 27 pulgadas", "precio": 350},
    ]
    print("\nDatos a exportar:")
    print(sample_data)

    # 2. Creamos las instancias de nuestras estrategias concretas.
    json_strategy = JsonExportStrategy()
    csv_strategy = CsvExportStrategy()
    html_strategy = HtmlExportStrategy()

    # 3. Creamos el Contexto (ReportGenerator) con una estrategia inicial (JSON).
    print("\nInicializando el generador de reportes con la estrategia JSON.")
    report_generator = ReportGenerator(strategy=json_strategy)

    # 4. Generamos y mostramos el reporte. El contexto usa la estrategia JSON.
    json_report = report_generator.generate_report(sample_data)
    print("\n--- Reporte en formato JSON ---")
    print(json_report)
    print("-----------------------------\n")

    # 5. Cambiamos la estrategia en tiempo de ejecución a CSV. ¡Esta es la clave del patrón!
    report_generator.set_strategy(csv_strategy)

    # 6. Generamos el reporte de nuevo. Ahora el contexto usa la estrategia CSV.
    csv_report = report_generator.generate_report(sample_data)
    print("\n--- Reporte en formato CSV ---")
    print(csv_report)
    print("----------------------------\n")

    # 7. Cambiamos la estrategia una vez más a HTML.
    report_generator.set_strategy(html_strategy)

    # 8. Generamos el reporte final. El contexto ahora usa la estrategia HTML.
    html_report = report_generator.generate_report(sample_data)
    print("\n--- Reporte en formato HTML ---")
    print(html_report)
    print("-----------------------------\n")

    print("--- Fin de la demostración ---")

if __name__ == "__main__":
    main()