import csv

from accounts.models import Account
from consumers.models import Consumer

def ingest_data(csv_data):
    csv_reader = csv.reader(csv_data.read().decode('utf-8').splitlines())
    next(csv_reader)
    accounts_to_create = []
    for row in csv_reader:
        consumer, created = Consumer.objects.get_or_create(
            name=row[3],
            address=row[4],
            ssn=row[5]
        )

        account = Account(
            client_reference_no=row[0],
            consumer=consumer,
            balance=row[1],
            status=row[2]
        )
        
        accounts_to_create.append(account)

    Account.objects.bulk_create(accounts_to_create)
        