from transactions.models import RawTransaction
import csv
from django.utils.dateparse import parse_datetime
from decimal import Decimal

with open('data_prueba_tecnica.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Truncar valores fuera del rango permitido
        amount = Decimal(row['amount'])
        if abs(amount) >= 10**14:
            amount = Decimal('99999999999999.99')

        created_at = parse_datetime(row['created_at']) if row['created_at'] else None
        paid_at = parse_datetime(row['paid_at']) if row['paid_at'] else None

        RawTransaction.objects.update_or_create(
            id=row['id'],
            name=row['name'],
            company_id=row['company_id'],
            amount=amount,
            status=row['status'],
            created_at=created_at,
            paid_at=paid_at
        )
