import httpx
from typing import Optional, Dict
from modules.auth import AuthResult
from utils.cookies import craft_cookie_header
from config.access_config import ENDPOINTS

def test_api_as_user(
    session: AuthResult,
    base_url: str,
    endpoint_key: str,
    resource_id: Optional[str] = None,
    payload: Optional[Dict] = None,
) -> Optional[httpx.Response]:
    try:
        endpoint_config = ENDPOINTS.get(endpoint_key)
        if not endpoint_config:
            print(f"[Error] Endpoint '{endpoint_key}' not found in config.")
            return None

        method = endpoint_config.get("method", "GET").upper()
        path = endpoint_config.get("path", "/")
        requires_id = endpoint_config.get("requires_id", False)

        if requires_id and resource_id:
            path = path.replace("{id}", resource_id)

        if not path.startswith("/"):
            path = "/" + path

        url = f"{base_url}{path.rstrip('/')}"

        headers = {
            "Content-Type": "application/json",
            "Cookie": craft_cookie_header(session.cookies),
        }

        client = httpx.Client(http2=True, timeout=10.0)

        if method == "GET":
            response = client.get(url, headers=headers)
        elif method == "POST":
            response = client.post(url, headers=headers, json=payload or {})
        elif method == "PUT":
            response = client.put(url, headers=headers, json=payload or {})
        elif method == "DELETE":
            response = client.delete(url, headers=headers)
        else:
            print(f"[Error] Unsupported method: {method}")
            return None

        return response

    except Exception as e:
        print(f"[Error] Error while testing '{endpoint_key}' as {session.email}: {e}")
        return None
