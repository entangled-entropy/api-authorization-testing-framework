from modules.auth import Authenticator, AuthResult
from utils.test_api import test_api_as_user
from config.testcases import TEST_CASES
from config.access_config import USERS, RESOURCES, ENDPOINTS, ROLE_HIERARCHY
from typing import Dict

def is_vertical_escalation(attacker_role: str, owner_role: str) -> bool:
    try:
        return ROLE_HIERARCHY.index(attacker_role) < ROLE_HIERARCHY.index(owner_role)
    except ValueError:
        return False

def check_privilege_escalation(base_url: str) -> None:
    print("[*] Starting Privilege Escalation Module...")

    auth = Authenticator(base_url)

    for case in TEST_CASES:
        user_id = case["user"]
        endpoint_key = case["endpoint"]
        resource_id = case["resource_id"]
        expected_statuses = case.get("expected_status", [403, 401, 404, 429, 409])
        unwelcomed_status = case.get("unwelcomed_status", [200, 201, 202, 204, 206])

        user = next((u for u in USERS if u["id"] == user_id), None)
        if not user:
            print(f"[!] User '{user_id}' not found in config.")
            continue

        session = auth.login(user["email"], user["password"])
        if not session:
            print(f"[!] Login failed for user '{user_id}'.")
            continue

        print(f"\n\n[*] Logged in as {user_id}, testing '{endpoint_key}' on resource '{resource_id}'")

        # Determine the resource type from ENDPOINTS config
        endpoint_def = ENDPOINTS.get(endpoint_key)
        if not endpoint_def:
            print(f"[!] Endpoint definition for '{endpoint_key}' not found.")
            continue

        resource_type = endpoint_def["resource_type"]
        resource_map = RESOURCES.get(resource_type, {})
        resource_info = resource_map.get(resource_id, {})
        if not resource_info:
            print(f"[!] Resource '{resource_id}' not found in '{resource_type}'. Skipping.")
            continue

        owner_ids = resource_info.get("access", [])

        response = test_api_as_user(
            session=session,
            base_url=base_url,
            endpoint_key=endpoint_key,
            resource_id=resource_id
        )

        if response:
            status = response.status_code
            if status in expected_statuses:
                print(f"[+] PASSED: Status {status} for user '{user_id}' on '{endpoint_key}'")
            elif status in unwelcomed_status:
                print(f"[-] FAILED: Unauthorized access granted with Status {status}")
                # Determine escalation type
                owner_roles = [u["role"] for u in USERS if u["id"] in owner_ids]
                attacker_role = user["role"]
                if any(is_vertical_escalation(attacker_role, owner_role) for owner_role in owner_roles):
                    print("=> Vertical Privilege Escalation Detected")
                else:
                    print("=> Horizontal Privilege Escalation Detected")
            else:
                print(f"[!] WARNING: Unexpected Status {status}")
        else:
            print(f"[!] No response for user '{user_id}' on '{endpoint_key}'")
