import httpx
from typing import Dict, Optional
from utils.cookies import craft_cookie_header
class AuthResult:
    # store response status, cookies n tokens
    def __init__(self,email: str, password: str, status_code: int, cookies: Dict[str, str]):
        self.status_code = status_code if status_code else None
        if cookies:
            self.cookies = cookies
        else:
            self.cookies = None

        self.email = email
        self.password = password

    def as_dict(self) -> Dict[str, Optional[str]]:
        return {
            "email": self.email,
            "password": self.password,
            "status_code": self.status_code,
            # **self.cookies,
            "cookies": self.cookies
        }

class Authenticator:
    # handles login, please pass login url
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = httpx.Client(http2=True, timeout=10.0)
        # self.csrf_cookie_name="csrfToken"
        self.cookies: Dict[str, str] = {}

    def _get_csrf_cookie(self) -> Optional[str]:
        # get csrf token by sending get request to login page
        try:
            csrf_api_endpoint = f"{self.base_url}/api/csrf-token"
            
            headers = {
            "Content-Type": "application/json",
            }

            response = self.session.post(csrf_api_endpoint, headers=headers, json={})
            
            cookies = {cookie.name: cookie.value for cookie in self.session.cookies.jar}
            # csrf_token = self.session.cookies.get(self.csrf_cookie_name)
            
            if not cookies:
                print("[Warning] No cookies returned from CSRF endpoint.")
                
            return cookies
            # return csrf_token
            
        except Exception as e:
            print(f"[error] no login page found {e}")
            return None

    def login(self, email: str, password: str) -> AuthResult:
        # login with credentials and capture tokens/cookies
        csrf_cookies = self._get_csrf_cookie()
        if not csrf_cookies:
            print(f"[Warning] No CSRF Token found, proceding without it")
        
        login_url = f"{self.base_url}/api/auth/login"
        headers = {
            "Content-Type": "application/json",
            "Cookie": craft_cookie_header(csrf_cookies),
        }

        payload = {"email": email, "password": password}

        try:
            response = self.session.post(login_url, headers=headers, json=payload)

            cookies = {cookie.name: cookie.value for cookie in self.session.cookies.jar}
            return AuthResult(email, password, response.status_code, cookies)
        except Exception as e:
            print(f"[Error] {e}")
            return None
