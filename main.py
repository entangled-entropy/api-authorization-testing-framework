from modules.auth import Authenticator, AuthResult
from modules.access_control import test_endpoint_access
from typing import Dict, Optional
from config.users_config import USERS
from config.endpoints_config import ENDPOINTS

BASE_URL = "https://pengate-staging.quarksek.com"
BASE_URL.rstrip('/')

def login_all_users(authenticator: Authenticator) -> dict:
    user_sessions = {}
    
    for user in USERS:
        role = user.get("role")
        user_id = user.get("id")
        email = user.get("email")
        password = user.get("password")

        print(f"Logging in {user_id} ({email})")
        result = authenticator.login(email, password)

        if isinstance(result, AuthResult):
            user_sessions[user_id] = {
                "session": result,
                "role": role,
                "email": email,
            }
        else:
            print(f"Failed to login {user_id} ({email})")
    return user_sessions


def main() -> None:
    print("\nStarting Module...")

    auth = Authenticator(BASE_URL)
    user_sessions = login_all_users(auth)

    print("\nRunning endpoint access tests...")
    test_endpoint_access(user_sessions, BASE_URL, ENDPOINTS)


if __name__ == "__main__":
    main()