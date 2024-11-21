import csv
from transactions.models import RawTransaction

# Consulta todos los registros de RawTransaction
transactions = RawTransaction.objects.all().values()

# Verificamos si hay transacciones para exportar
if transactions:
    # Abrimos el archivo y escribimos los datos
    with open('extracted_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=transactions[0].keys())
        writer.writeheader()
        writer.writerows(transactions)

    print("Datos exportados exitosamente a 'extracted_data.csv'")
else:
    print("No hay transacciones para exportar.")
