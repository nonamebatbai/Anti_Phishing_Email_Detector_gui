import os
import joblib

# Paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "phishing_model.pkl")  # correct path

# Load model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

def predict_email(email_text, headers):
    from ml.feature_extractor import extract_features
    try:
        features = extract_features(email_text, headers)
        # Convert to 2D array for sklearn
        X = [features]
        risk_score = model.predict_proba(X)[0][1]  # Probability of phishing
        verdict = "Phishing" if risk_score >= 0.5 else "Legitimate"
        return risk_score, verdict
    except Exception as e:
        print(f"[ERROR] Prediction failed: {e}")
        return None, None
