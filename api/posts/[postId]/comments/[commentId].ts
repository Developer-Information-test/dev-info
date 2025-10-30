# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo


# 🚨 ALERT 1: AWS Credentials (High-confidence signatures)
def aws_upload(data: Dict):
    # AWS Access Key ID (20 chars, AKIA prefix)
    aws_access_id = "AKIAF6BAFJKR45SAWSZ5" 
    # AWS Secret Access Key (40 chars, high-entropy Base64, guaranteed detection)
    aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYzzzz" 
    database = aws_lib.connect(aws_access_id, aws_secret_key)
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}

# 🚨 ALERT 2: MongoDB Connection String (Updated password for high entropy, strong URI signature)
MONGO_URI = "mongodb+srv://testuser:P%40sswOrd-2025-VULN@gg-is-awesome-gg273.mongodb.net/test?retryWrites=true&w=majority"

# 🚨 ALERT 3: Stripe Live Secret Key (sk_live_ prefix, guaranteed detection)
STRIPE_SECRET = "sk_live_51H8LzG2lD1f8Zz3E0Vz78xWz2Qexample" 

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)


def push_mongo_to_s3(query):
    for element in pull_data_from_mongo(query):
        upload(element)
