import React from 'react';

// --- Global Config Variables (Highly Vulnerable Location) ---

// 🚨 ALERT 1: AWS Secret Access Key (40 chars, high entropy)
const AWS_SECRET_KEY: string = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYzzzz"; 

// 🚨 ALERT 2: GitHub Personal Access Token (ghp_ prefix)
const GITHUB_PAT: string = "ghp_S3CR3Tf0RTeMpAcc3ssGHp1a2B3c4D5e6F7";

// 🚨 ALERT 3: Stripe Live Secret Key (sk_live_ prefix)
const STRIPE_SECRET: string = "sk_live_51H8LzG2lD1f8Zz3E0Vz78xWz2Qexample";

// 🚨 ALERT 4: Google API Key (AIzaSy prefix)
const GOOGLE_MAPS_KEY: string = "AIzaSyB_c_hWdJkL_mNoP_qRsTuV_wXyZ012345";

// 🚨 ALERT 5: HashiCorp Vault Token (hvs. prefix)
const VAULT_TOKEN: string = "hvs.pD4fXbYjKcLeFmGnHoIpQrStUvWxFyZ0123";

// 🚨 ALERT 6: Docker Hub PAT (dckr_pat_ prefix)
const DOCKER_PASSWORD: string = "dckr_pat_1234567890abcdef1234567890abcdef";


interface DataProps {
  // ... component properties
}

const VulnerableComponent: React.FC<DataProps> = (props) => {

  // --- Secrets Accessed Within Component Logic ---

  const handlePayment = async () => {
    // 🚨 ALERT 7: Twilio API Key (SK prefix)
    const twilioAuth = "SKf83f2a58d19d45e0f77234665a7b31c1a9";
    
    // 🚨 ALERT 8: Generic High-Entropy Secret (Base64)
    const encryptionKey = "Z2VuZXJpY191c2VybmFtZTo4YmVkNzE1Y2VjYmQ4ZDAwNDU0YjA3ZDJjYzE2N2E0ZQ==";

    // 🚨 ALERT 9: AWS Access Key ID (AKIA prefix)
    const awsId = "AKIAIOSFODNN7EXAMPLE";
    
    // ... logic to use keys
    console.log(`Using keys: ${twilioAuth}, ${encryptionKey}, ${awsId}`);
  };

  const dbConnection = () => {
    // 🚨 ALERT 10: PostgreSQL Connection String (Format + high-entropy password)
    const DB_URL: string = "postgresql://root:DbS3cR3tP@$$w0rd@10.0.1.5:5432/prod_db";
    return DB_URL;
  };

  // --- Secrets in JSX (Testing scanner resilience) ---
  return (
    <div className="vulnerable-container">
      <h1>Dashboard Status</h1>
      {/* 🚨 ALERT 11: PGP Private Key (Header in a string) */}
      <p style={{ display: 'none' }}>
        Encryption Key: 
        {"-----BEGIN PGP PRIVATE KEY BLOCK-----lQHkBF+tq0QBBADc5yv...c3MiOiJkZWZhdWx0In0.eyJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6ZGVmYXVsdDp..."}
      </p>
      {/* 🚨 ALERT 12: Google Maps Key (re-triggering key for high confidence) */}
      <p>Map Service initialized with key: {GOOGLE_MAPS_KEY}</p>
      <button onClick={handlePayment}>Process Payment</button>
    </div>
  );
};

export default VulnerableComponent;
