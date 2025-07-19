from collections import defaultdict
from typing import List, Dict

def print_security_summary(findings: List[Dict]) -> None:
    print("\n" + "=" * 50)
    print("[*] SECURITY FINDINGS SUMMARY")
    print("=" * 50)

    total = len(findings)
    print(f"Total vulnerabilities found: {total}")
    
    if total == 0:
        print("\n[+] No vulnerabilities found.")
        return

    grouped = defaultdict(list)
    for f in findings:
        grouped[f["type"]].append(f)

    for vuln_type, items in grouped.items():
        print(f"\n[!] {vuln_type}: {len(items)}")
        for item in items:
            print(f"\n  - User: {item.get('user', 'N/A')} (Role: {item.get('role', 'N/A')})"
                  f"\n    Endpoint: {item.get('endpoint', 'N/A')}"
                  f"\n    Resource: {item.get('resource', 'N/A')}"
                  f"\n    Payload: {item.get('payload', None)}"
                  f"\n    Status: {item.get('status', 'N/A')}")

