import os
import time
import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
from ml.feature_extractor import extract_features

# ---------------- PATHS ----------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATASET_PATH = os.path.join(BASE_DIR, "data", "phishing_dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "phishing_model.pkl")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "data")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ---------------- LOAD DATASET ----------------
df = pd.read_csv(DATASET_PATH)
if "label" not in df.columns:
    raise ValueError("Dataset must have a 'label' column (0=Legit,1=Phishing)")

X = []
y = df["label"].tolist()

# ---------------- FEATURE EXTRACTION ----------------
print("[INFO] Extracting features from emails...")
for index, row in df.iterrows():
    email_text = row.get("email_text", "")
    headers = row.get("headers", {})  # Optional: use headers column if exists
    if not isinstance(headers, dict):
        headers = {}
    features = extract_features(email_text, headers)
    X.append(features)

X_df = pd.DataFrame(X)

# ---------------- LOAD TRAINED MODEL ----------------
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Trained model not found at {MODEL_PATH}")

with open(MODEL_PATH, "rb") as f:
    model = joblib.load(f)

# ---------------- PREDICTIONS ----------------
y_pred = model.predict(X_df.values)
y_prob = model.predict_proba(X_df.values)[:, 1]

# ---------------- ACCURACY ----------------
acc = accuracy_score(y, y_pred)
print(f"[INFO] Model Accuracy: {acc:.4f}")

# ---------------- CONFUSION MATRIX ----------------
cm = confusion_matrix(y, y_pred)
print("[INFO] Confusion Matrix:")
print(cm)

# Timestamp for unique filenames
timestamp = time.strftime("%Y%m%d_%H%M%S")
cm_path = os.path.join(OUTPUT_FOLDER, f"confusion_matrix_{timestamp}.png")
roc_path = os.path.join(OUTPUT_FOLDER, f"roc_auc_curve_{timestamp}.png")

# Plot Confusion Matrix
plt.figure(figsize=(5,5))
plt.imshow(cm, cmap="Blues", interpolation="nearest")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i,j], ha='center', va='center', color='red', fontsize=14)
plt.tight_layout()
plt.savefig(cm_path, dpi=150)
plt.close()

# ---------------- ROC / AUC ----------------
roc_auc = roc_auc_score(y, y_prob)
fpr, tpr, thresholds = roc_curve(y, y_prob)

plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.4f}", color='blue', linewidth=2)
plt.plot([0,1], [0,1], linestyle="--", color='gray')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")
plt.tight_layout()
plt.savefig(roc_path, dpi=150)
plt.close()

print(f"[INFO] ROC AUC: {roc_auc:.4f}")
print(f"[INFO] Plots saved in {OUTPUT_FOLDER} as:\n - {os.path.basename(cm_path)}\n - {os.path.basename(roc_path)}")
print("[INFO] Evaluation completed successfully!")
