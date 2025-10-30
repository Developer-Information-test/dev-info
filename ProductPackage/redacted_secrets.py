# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo


def aws_upload(data: Dict):
    # 🚨 ALERT 1: AWS Access Key and Secret Key (High-confidence signatures)
    # The scanner will flag both the AKIA ID (20 chars) and the Secret Key (40 chars, high entropy).
    aws_access_key = "AKIAF6BAFJKR45SAWSZ5" 
    aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYzzzz" 
    
    database = aws_lib.connect(aws_access_key, aws_secret_key)
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}

# 🚨 ALERT 2: MongoDB Connection String (Strong URI signature with high-entropy password)
MONGO_URI = "mongodb+srv://testuser:P%40sswOrd-2025-VULN@gg-is-awesome-gg273.mongodb.net/test?retryWrites=true&w=majority"

# 🚨 ALERT 3: GitHub Personal Access Token (Distinct 'ghp_' prefix)
GITHUB_TOKEN = "ghp_S3CR3Tf0RTeMpAcc3ssGHp1a2B3c4D5e6F7"

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)


def push_mongo_to_s3(query):
    for element in pull_data_from_mongo(query):
        upload(element)
