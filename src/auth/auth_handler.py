import jwt
from decouple import config


# JWT_SECRET = config("secret")
JWT_SECRET = 'nRfzgTAOMtwaW9ezqnzNyzG5LAfBYcPDRHzSiwtkePin'
    
def signJWT(email: str, code: str,surname: str, name: str, picture: str) -> str:
    payload = {
        "Email": email,
        "Code": code,
        "Surname": surname,
        "Name": name,
        "Picture": picture
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return decoded_token
    except:
        return {}