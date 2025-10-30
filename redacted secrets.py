"""
This file is designed to generate the maximum number of high-confidence 
alerts from a secret scanning tool by using valid vendor signatures and formats.
"""

# --- 1. Cloud Provider Credentials ---
# 🚨 ALERT: AWS Secret Access Key (40 characters, high-entropy)
AWS_PROD_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY01234567"
# 🚨 ALERT: AWS Access Key ID (20 characters, AKIA prefix)
AWS_PROD_ACCESS_ID = "AKIAIOSFODNN7EXAMPLE"
# 🚨 ALERT: Azure Storage Connection String (Identified by format and 'AccountKey=...')
AZURE_STORAGE_CONN = "DefaultEndpointsProtocol=https;AccountName=prodstorage;AccountKey=aZr3S3cR3tPa$$w0rd+Zm9vYmFyMTIzNDU2Nzg5MA==;EndpointSuffix=core.windows.net"
# 🚨 ALERT: Google API Key (Identified by the 'AIzaSy' prefix)
GCP_MAPS_API_KEY = "AIzaSyB_c_hWdJkL_mNoP_qRsTuV_wXyZ012345"


# --- 2. Version Control & CI/CD Tokens ---
# 🚨 ALERT: GitHub Personal Access Token (Identified by the distinct 'ghp_' prefix)
GITHUB_TOKEN = "ghp_S3CR3Tf0RTeMpAcc3ssGHp1a2B3c4D5e6F7"
# 🚨 ALERT: GitLab Personal Access Token (Identified by the 'glpat-' prefix)
GITLAB_DEPLOY_TOKEN = "glpat-aBcD1E2fG3hI4jK5lM6nO7pQ8rS9tU0vW1xY2Z3"
# 🚨 ALERT: Docker Hub PAT (Identified by the 'dckr_pat_' prefix)
DOCKER_HUB_PASSWORD = "dckr_pat_1234567890abcdef1234567890abcdef"


# --- 3. Database and Connection Strings ---
# 🚨 ALERT: MongoDB Connection String (Identified by 'mongodb+srv://' and high-entropy password)
MONGO_URI_PROD = "mongodb+srv://user:P%40sswOrd-2025-VULN@prod-cluster.mongodb.net/prod?retryWrites=true&w=majority"
# 🚨 ALERT: PostrgeSQL Connection String (Identified by 'postgresql://' and hardcoded password)
POSTGRES_CONN_STRING = "postgresql://root:DbS3cR3tP@$$w0rd@10.0.1.5:5432/prod_db"


# --- 4. Messaging and Payments ---
# 🚨 ALERT: Stripe Live Secret Key (Identified by the distinct 'sk_live_' prefix)
STRIPE_KEY = "sk_live_51H8LzG2lD1f8Zz3E0Vz78xWz2Qexample"
# 🚨 ALERT: Twilio API Key (Identified by the 'SK' prefix)
TWILIO_API_KEY = "SKf83f2a58d19d45e0f77234665a7b31c1a9"
# 🚨 ALERT: SendGrid API Key (Identified by the 'SG.' prefix and structured format)
SENDGRID_API_KEY = "SG.s3cr3t.k3Y.f0r.EmAil1Ng.t0K3N"


# --- 5. Cryptographic and Generic Secrets ---
# 🚨 ALERT: RSA Private Key (Identified by the distinct header '-----BEGIN RSA PRIVATE KEY-----')
RSA_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKCAQEAwZ...jC7A1g==
-----END RSA PRIVATE KEY-----
"""
# 🚨 ALERT: JSON Web Token (JWT) (Identified by 'eyJhbGciOi' header structure)
JWT_SECRET = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIwMTAxMjMifQ.SflKxwR...XWd"
# 🚨 ALERT: HashiCorp Vault Token (Identified by the 'hvs.' prefix)
VAULT_TOKEN = "hvs.pD4fXbYjKcLeFmGnHoIpQrStU
