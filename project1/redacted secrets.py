
# --- 1. Cloud Provider Secrets (AWS, GCP, Azure) ---
# 🚨 ALERT: AWS Secret Access Key (40 characters, high-entropy, definitive signature)
AWS_PROD_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY01234567"
# 🚨 ALERT: AWS Access Key ID (20 characters, AKIA prefix)
AWS_PROD_ACCESS_ID = "AKIAIOSFODNN7EXAMPLE"
# 🚨 ALERT: Azure Storage Connection String (Identified by format: DefaultEndpointsProtocol=...)
AZURE_STORAGE_CONN = "DefaultEndpointsProtocol=https;AccountName=prodstorage;AccountKey=aZr3S3cR3tPa$$w0rd+Zm9vYmFyMTIzNDU2Nzg5MA==;EndpointSuffix=core.windows.net"
# 🚨 ALERT: Google API Key (Identified by AIzaSy prefix)
GCP_MAPS_API_KEY = "AIzaSyB_c_hWdJkL_mNoP_qRsTuV_wXyZ012345"


# --- 2. Version Control & CI/CD Tokens ---
# 🚨 ALERT: GitHub Personal Access Token (Identified by 'ghp_')
GITHUB_TOKEN = "ghp_S3CR3Tf0RTeMpAcc3ssGHp1a2B3c4D5e6F7"
# 🚨 ALERT: GitLab Personal Access Token (Identified by 'glpat-')
GITLAB_DEPLOY_TOKEN = "glpat-aBcD1E2fG3hI4jK5lM6nO7pQ8rS9tU0vW1xY2Z3"
# 🚨 ALERT: Docker Hub PAT (Identified by 'dckr_pat_')
DOCKER_HUB_PASSWORD = "dckr_pat_1234567890abcdef1234567890abcdef"


# --- 3. Database and Connection Strings ---
# 🚨 ALERT: MongoDB Connection String (Identified by format and high-entropy password)
MONGO_URI_PROD = "mongodb+srv://user:P%40sswOrd-2025-VULN@prod-cluster.mongodb.net/prod?retryWrites=true&w=majority"
# 🚨 ALERT: PostrgeSQL Connection String (Identified by format and hardcoded password)
POSTGRES_CONN_STRING = "postgresql://root:DbS3cR3tP@$$w0rd@10.0.1.5:5432/prod_db"


# --- 4. Messaging and Payments ---
# 🚨 ALERT: Stripe Live Secret Key (Identified by 'sk_live_')
STRIPE_KEY = "sk_live_51H8LzG2lD1f8Zz3E0Vz78xWz2Qexample"
# 🚨 ALERT: Twilio API Key (Identified by 'SK' prefix)
TWILIO_API_KEY = "SKf83f2a58d19d45e0f77234665a7b31c1a9"
# 🚨 ALERT: SendGrid API Key (Identified by 'SG.')
SENDGRID_API_KEY = "SG.s3cr3t.k3Y.f0r.EmAil1Ng.t0K3N"


# --- 5. Cryptographic and Generic Secrets ---
# 🚨 ALERT: RSA Private Key (Identified by distinct header)
RSA_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKCAQEAwZ...jC7A1g==
-----END RSA PRIVATE KEY-----
"""
# 🚨 ALERT: JSON Web Token (JWT) (Identified by Base64 structure and header/payload pattern)
JWT_SECRET = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIwMTAxMjMifQ.SflKxwR...XWd"
# 🚨 ALERT: HashiCorp Vault Token (Identified by 'hvs.' prefix)
VAULT_TOKEN = "hvs.pD4fXbYjKcLeFmGnHoIpQrStUvWxFyZ0123"
# 🚨 ALERT: Generic High-Entropy Key (Identified by Base64 encoding and length)
GENERIC_APP_SECRET = "Z2VuZXJpY191c2VybmFtZTo4YmVkNzE1Y2VjYmQ4ZDAwNDU0YjA3ZDJjYzE2N2E0ZQ=="
# 🚨 ALERT: Generic Password Hash (Bcrypt hash)
USER_PASSWORD_HASH = "$2a$10$vYgC1r.iO6vL...xY9F0nE7.rA" 

# Other variables
APP_VERSION = "2.3.1"
API_URL = "https://api.internal.com/v1"
