from transactions.models import RawTransaction, Company, Charge

def transform_data():
    for transaction in RawTransaction.objects.all():
        company, _ = Company.objects.get_or_create(
            id=transaction.company_id,
            name=transaction.name
        )
        Charge.objects.create(
            id=transaction.id,
            company=company,
            amount=transaction.amount,
            status=transaction.status,
            created_at=transaction.created_at,
            updated_at=transaction.paid_at
        )
