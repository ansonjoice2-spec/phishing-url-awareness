# EWB Phishing URL Awareness Checker

## Overview

Phishing is a social engineering attack where malicious actors use deceptive links to trick individuals into divulging sensitive credentials, financial data, or one-time passwords (OTPs). The EWB Phishing URL Awareness Checker is a command-line defensive utility that inspects URL text for common structural indicators and anomalies often found in deceptive links. This tool performs static lexical analysis only and does not establish network connections or visit target websites.

## Features

* **@ Symbol Detection:** Identifies `@` characters within the URL string that can be used by browsers to discard preceding authentication text and mask the true host destination.

* **Length Anomaly Flagging:** Flags URLs exceeding 100 characters, a common tactic used to obscure true endpoints on mobile and constrained displays.

* **IPv4 Hostname Check:** Detects numeric IPv4 addresses used directly as hostnames instead of standard domain names.

* **Hostname Segment / Subdomain Analysis:** Identifies complex hostnames containing 5 or more segments separated by dots.

* **Punycode (IDN) Marker Detection:** Inspects hostnames for `xn--` indicators commonly utilized in homograph attacks with look-alike non-ASCII characters.

* **Insecure Scheme Warning:** Detects unencrypted `http://` schemes, noting that `https://` alone does not guarantee authenticity.

* **Continuous Evaluation Loop (Improvement A):** Supports multiple URL inspections in a single session without requiring a restart, complete with a clean exit command (`q`, `quit`, `exit`).

* **Resilient Exception Handling (Improvement C):** Wraps URL parsing in a `try...except ValueError` block to safely catch malformed inputs (such as improper IPv6 bracket formatting) without crashing.

## Requirements

* Python 3.10 or later

* No third-party packages or external dependencies required (uses standard library modules `re` and `urllib.parse`).

## How to Run

### Windows

```
python phishing_checker.py

```

*(or use `py phishing_checker.py` if python is not mapped to PATH directly)*

### macOS / Linux

```
python3 phishing_checker.py

```

## Example Output

```
=============================================
   EWB Phishing URL Awareness Checker
   Text checks only — does not open URLs
=============================================

Enter a sample URL to inspect (or 'q' to quit): http://192.0.2.10/account

Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.

Reminder: Never enter passwords from unexpected links.

```

## Testing

The tool was evaluated against the standardized benchmark test cases:

| \# | Input | Expected Result | Actual Result | Status | 
| ----- | ----- | ----- | ----- | ----- | 
| 1 | `https://www.example.com/login` | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS | 
| 2 | `http://192.0.2.10/account` | IP address + HTTP | Uses an IP address instead of a familiar domain.    Uses HTTP. HTTPS alone does not prove trust. | PASS | 
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP | Contains an @ symbol; inspect carefully.    Uses HTTP. HTTPS alone does not prove trust. | PASS | 
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Contains many hostname segments/subdomains. | PASS | 
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Contains a punycode-style hostname. | PASS | 

*Full evidence log and detailed observations are documented in `tests/test_samples.md`.*

## Screenshots

Terminal run demonstration:

Test suite evidence: it is stored in test_result.png file in screenshot section

Sample run evidance: it is stored in sample_run.png file in screenshot section 

## Improvements

1. **Interactive Session Loop (Improvement A):**

   * *Change:* Replaced the single-run execution flow with an interactive `while True` loop that accepts multiple sequential URLs and terminates gracefully when `q`, `quit`, or `exit` is entered.

   * *Why:* Significantly improves usability and testing speed by eliminating the need to restart the Python script for each test.

   * *Testing:* Tested repeated inputs with valid URLs, empty inputs, and exit terms (`q`, `quit`).

2. **Safe Input Exception Handling (Improvement C):**

   * *Change:* Enclosed `urlparse(candidate)` within a `try...except ValueError` block.

   * *Why:* Prevents the program from crashing abruptly with an unhandled exception when processing malformed URL structures (e.g., `http://[bad`).

   * *Testing:* Tested with malformed input `http://[bad` to verify that the program outputs a clean error message (`"This text is not a valid URL format."`) and remains operational.

## Limitations

This program is an educational awareness utility strictly limited to static textual heuristics. It does not:

* Establish network connections, resolve DNS queries, or scan server reputations.

* Inspect page source code, execute sandboxed analysis, or detect zero-day exploits.

* Guarantee website safety. The output `"No listed warning signs found"` indicates only that the selected lexical flags were absent; it **does NOT** guarantee that a URL is legitimate or safe.

## Ethical Use

This project is intended strictly for defensive security education and link analysis awareness. All testing was performed using reserved documentation IP ranges (`RFC 5737`) and standard testing domain extensions (`.invalid`, `.example`). Do not use this tool to assist in constructing deceptive URLs or harvest credentials.

## Author

* **Author:** Anson joice

* **Track:** Cybersecurity Mini Project / Internship

* **Provider:** EWB Courses
