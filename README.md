# 🛡️ Anti‑Phishing Email Detector

Analyzes email content, headers, and links to identify phishing attacks, calculate risk scores, store history, and visualize ML evaluation results.

## 📸 Screenshots
![Screenshot 1]()

![Screenshot 1]()

![Screenshot 1]()

![Screenshot 1]()

![Screenshot 1]()

## 🏷️ Tags

`#phishing` `#email-security` `#cybersecurity` `#machine-learning`
`#ai-security` `#spam-detection` `#fraud-detection` `#python` `#sqlite`

## 👨‍💻 Developed By

**Syed Shaheer Hussain**
© **Copyright 2026 – All Rights Reserved**

## 📌 Introduction

Email phishing is one of the **most dangerous cyber attacks** today.
Attackers send fake emails pretending to be banks, companies, or trusted services to:

* Steal passwords
* Hack accounts
* Leak personal data
* Commit financial fraud

This project provides a **complete AI‑powered solution** to detect such phishing emails **before damage happens**.

## 🎯 Mission

✅ Protect users from phishing
✅ Educate users about email threats
✅ Use Machine Learning for smart detection
✅ Provide history, analytics, and transparency
✅ Build a scalable cybersecurity product

## 🌍 Why This Project Was Made

### ❓ Problem

* Millions of phishing emails daily
* Humans fail to identify fake emails
* Huge financial & data losses

### 💡 Solution

* Automated ML‑based phishing detection
* Risk scoring instead of yes/no
* GUI dashboard for non‑technical users

## 📈 Market Value & Importance

| Area | Value |
| --- | --- |
| Cybersecurity Market | $300+ Billion    |
| Phishing Attacks     | #1 attack vector |
| AI Security Tools    | High demand      |
| Academic Value       | FYP / Research   |
| Commercial Value     | SaaS / Product   |

👉 **This project can be converted into:**

* SaaS product
* Browser extension
* Enterprise email scanner
* API‑based security service

## 🧠 What is Phishing?

### 📧 Phishing

A cyber attack where fake emails trick users into revealing:

* Passwords
* OTPs
* Bank details
* Login credentials

### 🧪 Example

> “Your account is suspended. Click here to verify.”

## 🛡️ What is Anti‑Phishing?

Anti‑phishing systems:

* Analyze email content
* Detect suspicious patterns
* Block or warn users
* Reduce human error

## 🏗️ Project Architecture

```
User
 │
 │ Email Input
 ▼
GUI Dashboard (Tkinter)
 │
 ├─ Email Parser
 ├─ Feature Extractor
 ├─ NLP Analyzer
 ├─ ML Classifier
 │
 ▼
Prediction Engine
 │
 ├─ Risk Score
 ├─ Verdict
 │
 ▼
SQLite Database
 │
 ├─ Email History
 └─ Evaluation Data

```

## 🔁 Flowchart (Text)

```
Start
 ↓
Paste Email
 ↓
Parse Headers + Body
 ↓
Extract Features
 ↓
ML Model Prediction
 ↓
Risk Score Calculation
 ↓
Verdict (Safe / Phishing)
 ↓
Save to Database
 ↓
Display Result
 ↓
End

```

## 📁 Folder Structure Explained

```
anti_phishing_email_detector/
│
├── main.py                 → Project entry point
├── gui.py                  → GUI Dashboard
├── classifier.py           → ML prediction logic
├── database.py             → SQLite database
├── email_parser.py         → Email header parsing
├── feature_extractor.py    → Feature extraction
├── nlp_analyzer.py         → NLP analysis
├── utils.py                → Helper utilities
├── requirements.txt        → Dependencies
│
├── data/
│   ├── detector.db         → Email history DB
│   ├── phishing_dataset.csv
│   ├── confusion_matrix.png
│   └── roc_auc_curve.png
│
├── models/
│   └── phishing_model.pkl  → Trained ML model
│
└── ml/
    ├── train_model.py      → Model training
    └── evaluate_model.py   → Model evaluation

```

## ⚙️ Technologies Used

### 🧑‍💻 Programming Languages

* Python 🐍

### 🤖 Machine Learning

* Scikit‑Learn
* Random Forest Classifier

### 📊 Data & Storage

* SQLite3
* CSV Dataset

### 🖥️ GUI

* Tkinter
* Pillow (Images)

### 📈 Visualization

* Matplotlib
* ROC / AUC
* Confusion Matrix

## 🧪 Features Implemented

### ✅ Core Features

1. Email content analysis
2. Header inspection
3. URL & domain checks
4. NLP keyword analysis
5. Risk score generation

### ✅ ML Features

6. Real trained ML model
7. Model accuracy evaluation
8. Confusion matrix graph
9. ROC / AUC curve

### ✅ GUI Features

10. Email analyzer dashboard
11. Email history viewer
12. Evaluation plots viewer

## 🧩 Functions Overview

| Function | Purpose |
| --- | --- |
| `predict_email()`      | Predict phishing   |
| `extract_features()`   | Feature extraction |
| `save_email_history()` | Save results       |
| `get_email_history()`  | View history       |
| `train_model.py`       | Train ML           |
| `evaluate_model.py`    | Evaluate ML        |

## 🖥️ GUI Working

### 🧭 Tabs

1. **Analyze Email**
2. **Email History**
3. **ML Evaluation**

### 📌 How GUI Works

* Paste email
* Click Analyze
* Get verdict + score
* Saved automatically
* View history anytime
* View ML performance charts

## 🛠️ Installation Guide (Step‑By‑Step)

### 🔹 Step 1: Install Python

* Python **3.10+**
* Add to PATH

### 🔹 Step 2: Install Requirements

```bash
pip install -r requirements.txt

```

### 🔹 Step 3: Dataset

* Place `phishing_dataset.csv` in `data/`

## ▶️ How to Run (Step‑By‑Step)

### 1️⃣ Train Model

```bash
python ml/train_model.py

```

### 2️⃣ Evaluate Model

```bash
python ml/evaluate_model.py

```

### 3️⃣ Run Application

```bash
python main.py

```

## 🌐 Chrome / Web Hosting?

> ⚠️ **This is a Desktop Application**, not web‑hosted.

No:

* Host
* Username
* Password
* Browser login

👉 Future enhancement can convert it into:

* Flask / Django Web App
* Cloud SaaS
* Chrome Extension

## 🧪 How to Use

1. Open app
2. Paste email
3. Click **Analyze**
4. Read verdict
5. Check history
6. View evaluation

## ⚠️ Cautions

>[!caution]
> * Model accuracy depends on dataset
> * Not 100% guaranteed
> * Should be combined with awareness
> * Dataset bias possible

## 📚 What You Learn From This Project

### 🎓 Technical

* Machine Learning
* Feature engineering
* NLP basics
* GUI development
* SQLite database
* Model evaluation

### 🧠 Concepts

* Cybersecurity
* Phishing techniques
* AI security systems
* Risk‑based detection

## 🔮 Future Enhancements

🚀 Planned:

* Real‑time email scanning
* Browser extension
* Deep learning (LSTM)
* Online dashboard
* Feedback learning
* API service
* Cloud deployment

## 🧾 Disclaimer

>[!warning]
> This project is developed **for educational and research purposes only**.
> The developer is **not responsible for misuse** or damages caused by reliance solely on this tool.

## 📌 Important Notes

>[!important]
> * Always verify suspicious emails manually
> * Never click unknown links
> * Enable 2FA
> * Use password managers

## 🛡️ How to Stay Safe from Phishing

✅ Check sender email
✅ Avoid urgent language
✅ Don’t click random links
✅ Verify before login
✅ Use security tools

## 💎 Final Value Statement

>[!note]
> **This project demonstrates a complete real‑world AI cybersecurity solution combining Machine Learning, GUI, databases, and visualization — suitable for academic, professional, and commercial use.**
