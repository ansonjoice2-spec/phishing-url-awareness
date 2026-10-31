import re
from urllib.parse import urlparse

def inspect_url(raw_url):
    """
    Inspects URL text for common phishing indicators without visiting the site.
    Returns a list of findings/warnings.
    """
    url = raw_url.strip()
    findings = []
    
    # 0. Check for empty input
    if not url:
        return ["No URL entered."]
    
    # Prepend scheme if missing so urlparse can reliably extract the host
    candidate = url if "://" in url else "http://" + url
    
    # Safe parsing: prevents crash on malformed inputs like 'http://[bad'
    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]
        
    host = (parsed.hostname or "").lower()
    if not host:
        return ["Could not identify a hostname."]
    
    # Check 1: '@' symbol (browsers ignore text before '@', disguising true destination)
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")
        
    # Check 2: Length check (often used to obscure full URL)
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")
        
    # Check 3: Raw IPv4 address as hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append("Uses an IP address instead of a familiar domain.")
        
    # Check 4: Excessive hostname segments/subdomains (5 or more parts)
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append("Contains many hostname segments/subdomains.")
        
    # Check 5: Punycode marker (can be used for homograph/look-alike character tricks)
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")
        
    # Check 6: Insecure HTTP scheme
    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")
        
    # Fallback if no indicators are triggered
    if not findings:
        findings.append("No listed warning signs found. This does NOT prove safety.")
        
    return findings


def main():
    print("=" * 45)
    print("   Phishing URL Awareness Checker")
    print("   Text checks only — does not open URLs")
    print("=" * 45)
    
    while True:
        raw_url = input("\nEnter a sample URL to inspect (or 'q' to quit): ")
        
        # Check for quit signal
        if raw_url.strip().lower() in ("q", "quit", "exit","0","stop"):
            print("Exiting checker. Stay safe online!")
            break
            
        results = inspect_url(raw_url)
        
        print("\nResult:")
        for finding in results:
            print("- " + finding)
            
        print("\nReminder: Never enter passwords from unexpected links.\n Not provide your personal information or phone numbers etc")


main()