import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.feature_extractor import extract_features
import os

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASET_PATH = os.path.join(BASE_DIR, "data", "phishing_dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "phishing_model.pkl")

df = pd.read_csv(DATASET_PATH)

# Extract features for each email
X = []
y = df["label"].tolist()

print("[INFO] Extracting features for training...")
for idx, row in df.iterrows():
    email_text = row.get("email_text", "")
    headers = {}  # Fill headers if available
    features = extract_features(email_text, headers)
    X.append(features)

X_df = pd.DataFrame(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_df, y, test_size=0.2, random_state=42
)

# Train RandomForest model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Save trained model
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"✅ Model trained & saved at {MODEL_PATH}")
