import re
import tldextract

def extract_features(text, headers):
    features = {}

    # ---------- URL FEATURES ----------
    urls = re.findall(r"http[s]?://[^\s]+", text)
    suspicious_domains = 0

    for url in urls:
        ext = tldextract.extract(url)
        if ext.domain and len(ext.domain) > 15:
            suspicious_domains += 1

    features["suspicious_domains"] = suspicious_domains
    features["total_urls"] = len(urls)
    features["ip_in_url"] = sum(1 for u in urls if re.search(r"\d+\.\d+\.\d+\.\d+", u))

    # ---------- HEADER FEATURES ----------
    sender = headers.get("From", "")
    reply_to = headers.get("Reply-To", "")

    # Fix empty string issue
    if reply_to and sender:
        features["reply_to_mismatch"] = int(reply_to not in sender)
    else:
        features["reply_to_mismatch"] = 0

    features["missing_received"] = int("Received" not in headers)

    # ---------- CONTENT FEATURES ----------
    content = text.lower()
    subject = headers.get("Subject", "")

    phishing_words = [
        "verify", "account", "password", "urgent",
        "login", "bank", "click", "confirm"
    ]

    features["phishing_words_count"] = sum(content.count(w) for w in phishing_words)
    features["exclamation_count"] = content.count("!")
    features["dollar_signs"] = content.count("$")
    features["subject_all_caps"] = int(subject.isupper()) if subject else 0

    return list(features.values())
