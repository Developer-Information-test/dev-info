# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo


def aws_upload(data: Dict):
    # IMPORTANT: Credentials have been redacted for security.
    # Use environment variables or a secrets management tool.
    database = aws_lib.connect("REDACTED_AWS_ACCESS_KEY", "REDACTED_AWS_SECRET_KEY")
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}

# IMPORTANT: Credentials have been redacted for security.
# Use environment variables or a secrets management tool.
MONGO_URI = "mongodb+srv://<user>:<password>@<host>/<database>?retryWrites=true&w=majority"

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)


def push_mongo_to_s3(query):
    for element in pull_data_from_mongo(query):
        upload(element)
