def analyze_headers(headers):
    score = 0
    reasons = []

    from_addr = headers.get("From", "")
    reply_to = headers.get("Reply-To", "")

    if reply_to and reply_to not in from_addr:
        score += 0.3
        reasons.append("Reply-To mismatch")

    if "Received" not in headers:
        score += 0.2
        reasons.append("Missing Received headers")

    auth = headers.get("Authentication-Results", "")
    if "dkim=fail" in auth.lower():
        score += 0.3
        reasons.append("DKIM authentication failed")

    return score, reasons
