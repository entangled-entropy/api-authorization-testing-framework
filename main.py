from modules.privilege_escalation import check_privilege_escalation
from config.access_config import BASE_URL

def main():
    check_privilege_escalation(BASE_URL)

if __name__ == "__main__":
    main()