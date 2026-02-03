import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Auto-download required NLTK resources
for resource in ["punkt", "punkt_tab", "stopwords"]:
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(resource)

PHISHING_KEYWORDS = [
    "urgent", "verify", "account suspended", "click below",
    "reset password", "unauthorized", "confirm now"
]

def analyze_text(text):
    score = 0
    reasons = []

    if not text or len(text.strip()) == 0:
        return 0.0, ["Empty email body"]

    text_lower = text.lower()

    for word in PHISHING_KEYWORDS:
        if word in text_lower:
            score += 0.1
            reasons.append(f"Suspicious phrase detected: '{word}'")

    tokens = word_tokenize(text_lower)
    stop_words = set(stopwords.words("english"))
    filtered = [w for w in tokens if w.isalpha() and w not in stop_words]

    if len(filtered) < 20:
        score += 0.1
        reasons.append("Unusually short message body")

    return min(score, 0.6), reasons
