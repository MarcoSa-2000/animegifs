import jwt
import requests
from animegifs.distutils import errors

TOKEN = None
DATA = None


def authentication():
    try:
        response = requests.post(
            "https://enkidu-app-5a3qq2fqya-uc.a.run.app/key1", timeout=100
        )
    except requests.exceptions.Timeout:
        try:
            response = requests.post(
                "https://enkidu-app-5a3qq2fqya-uc.a.run.app/key2", timeout=25
            )
        except requests.exceptions.Timeout as exc:
            raise errors.AuthTimeout(exc)
    if response.status_code == 200:
        auth_key = response.json()["key"]
    else:
        exc = response.status_code
        raise errors.AuthError(exc)
    return auth_key


def access(update_list=False):
    global TOKEN
    global DATA

    if not TOKEN:
        TOKEN = authentication()

    if not DATA or update_list:
        decoded_json = jwt.decode(TOKEN, "enkidu-key", algorithms="HS512")
        data_url = list(decoded_json.keys())[0]
        DATA = requests.get(data_url).json()

    return DATA
