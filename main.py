from modules.privilege_escalation import check_privilege_escalation
from config.access_config import BASE_URL
from modules.security_summary import print_security_summary

def main():
    findings = [
        # Dummy Data
        
        # {
        #     "type": "SQL Injection",
        #     "user": "tester1",
        #     "role": "tester",
        #     "resource": "/api/search?query=",
        #     "endpoint": "search_query",
        #     "payload": "' OR 1=1 --",
        #     "status": 500
        # },
        
        # {
        #     "type": "XSS",
        #     "user": "admin",
        #     "role": "admin",
        #     "resource": "/api/comments",
        #     "endpoint": "post_comment",
        #     "payload": None,
        #     "status": 200
        # },
        
        # {
        #     "type": "SQL Injection",
        #     "user": "customer3",
        #     "role": "customer",
        #     "resource": "/api/products?filter='; DROP TABLE users; --",
        #     "endpoint": "filter_products",
        #     "payload": "; DROP TABLE users; --",
        #     "status": 500
        # }
    ]

    findings.extend(check_privilege_escalation(BASE_URL))
    # we can add more vuln modules and append findings like below
    # findings.extend(check_sql_injection(BASE_URL))
     
    print_security_summary(findings)

if __name__ == "__main__":
    main()