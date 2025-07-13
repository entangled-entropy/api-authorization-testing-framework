from typing import Dict, List, Union
from utils.test_api import test_api_as_user
from modules.auth import AuthResult


def is_privilege_lower(requester_role: str, owner_role: str) -> bool:
    hierarchy = ["customer", "tester"]
    try:
        return hierarchy.index(requester_role) < hierarchy.index(owner_role)
    except ValueError:
        return False


def test_endpoint_access(
    user_sessions: Dict[str, Dict],
    base_url: str,
    endpoints: Dict[str, Union[str, List[str]]]
) -> None:
    vertical_issues, horizontal_issues, passed, unexpected = [], [], [], []

    for endpoint, owners in endpoints.items():
        allowed_users = owners if isinstance(owners, list) else [owners]

        for user_id, user_info in user_sessions.items():
            is_allowed = "any" in allowed_users or user_id in allowed_users

            # Corrected: Accessing values via dict key
            session: AuthResult = user_info["session"]
            role: str = user_info["role"]

            print(f"\nTesting {endpoint} as {user_id} role:{role} allowed: {allowed_users}")

            response = test_api_as_user(session, base_url, endpoint)
            if not response:
                print("No response or request failed")
                unexpected.append((user_id, endpoint, "No response"))
                continue

            status = response.status_code

            if is_allowed and status == 200:
                print("PASSED – Authorized access")
                passed.append((user_id, endpoint))
            elif not is_allowed and status == 200:
                print("FAILED – VULNERABLE: Unauthorized access granted")
                owner_roles = [
                    user_sessions[o]["role"]
                    for o in allowed_users if o in user_sessions
                ]
                if any(is_privilege_lower(role, owner_role) for owner_role in owner_roles):
                    vertical_issues.append((user_id, endpoint))
                else:
                    horizontal_issues.append((user_id, endpoint))
            elif not is_allowed and status in (403, 401, 404, 409):
                print("PASSED – Access correctly denied")
                passed.append((user_id, endpoint))
            else:
                print(f"UNEXPECTED – Status: {status}")
                unexpected.append((user_id, endpoint, status))

    # Summary
    print("\nACCESS CONTROL TEST SUMMARY")
    print(f"Passed: {len(passed)}")
    print(f"Vertical Escalations: {len(vertical_issues)}")
    print(f"Horizontal Escalations: {len(horizontal_issues)}")
    print(f"Unexpected: {len(unexpected)}")
