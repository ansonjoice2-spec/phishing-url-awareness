# Test Results

Python version used: 3.10+ | Operating system: Windows / Linux / macOS | Date: 2026-10-31

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | https://www.example.com/login | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | http://192.0.2.10/account | IP address + HTTP | Uses an IP address instead of a familiar domain.<br>Uses HTTP. HTTPS alone does not prove trust. | PASS |
| 3 | http://example.com@sample.invalid/login | @ symbol + HTTP | Contains an @ symbol; inspect carefully.<br>Uses HTTP. HTTPS alone does not prove trust. | PASS |
| 4 | https://a.b.c.d.e.example.invalid/path | Many hostname segments | Contains many hostname segments/subdomains. | PASS |
| 5 | https://xn--example.invalid/ | Punycode-style hostname | Contains a punycode-style hostname. | PASS |

## Notes
- Testing confirmed that the program performs only passive text analysis without visiting any web addresses.
- Test 1 demonstrates a critical security takeaway: having zero listed indicators does not guarantee that a link is authentic or safe.
- Test 2 and Test 3 show that multiple suspicious indicators (e.g., raw IP addressing or embedded '@' symbols combined with plain HTTP) can trigger simultaneously on a single input string.
- Input validation correctly parsed non-standard URLs and caught edge cases without crashing.