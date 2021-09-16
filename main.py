import csv
from pprint import pprint
from uuid import uuid4
import os
from dotenv import load_dotenv

load_dotenv()

statement_file_name = os.getenv("STATEMENT_FILE_NAME")
transactions = []
print(statement_file_name)
with open(statement_file_name) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    for row in csv_reader:
        transaction = dict()
        transaction["_id"] = str(uuid4())
        for key, value in row.items():
            new_key = "_".join(key.strip().split(" ")).lower()
            new_value = value.rstrip() if key.strip()== "Narration" else value.strip()
            transaction[new_key] = new_value
        transactions.append(transaction)
csv_file.close()

print(f"Transactions of {statement_file_name} are below:")
pprint(transactions)