import httpx
from typing import Optional, Dict
from modules.auth import AuthResult 
from utils.cookies import craft_cookie_header

def test_api_as_user(
    session: AuthResult,
    base_url: str,
    endpoint: str,
    method: str = "GET",
    payload: Optional[Dict] = None,
    ) -> Optional[httpx.Response]:
    
    try:
        client = httpx.Client(http2=True, timeout=10.0)
        if not endpoint.startswith('/'):
            endpoint = '/' + endpoint

        url = f"{base_url}{endpoint.rstrip('/')}"

        headers = {
            "Content-Type": "application/json",
            "Cookie": craft_cookie_header(session.cookies),
        }

        if method.upper() == "GET":
            response = client.get(url, headers=headers)
        elif method.upper() == "POST":
            response = client.post(url, headers=headers, json=payload or {})
        # elif method.upper() == "PUT":
        #     response = client.put(url, headers=headers, json=payload or {})
        # elif method.upper() == "DELETE":
        #     response = client.delete(url, headers=headers)
        else:
            print(f"Unsupported method: {method}")
            return None

        return response

    except Exception as e:
        print(f"Error while testing {endpoint} as {session.email}: {e}")
        return None
