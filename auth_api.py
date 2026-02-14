import requests
from config import BACKEND_BASE_URL

def login_user(email: str, password: str):
    response = requests.post(
        f"{BACKEND_BASE_URL}/auth/login",
        data={
            "username": email,
            "password": password
        }
    )

    if response.status_code == 200:
        return response.json()["access_token"]

    return None


def register_user(email: str, password: str):
    try:
        response = requests.post(
            f"{BACKEND_BASE_URL}/auth/register",
            json={"email": email, "password": password},
            timeout=5
        )
        return response.status_code == 200
    except Exception:
        return False
