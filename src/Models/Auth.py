from typing import Any
from dataclasses import dataclass

@dataclass
class Root:
    iss: str
    azp: str
    aud: str
    sub: str
    hd: str
    email: str
    email_verified: bool
    at_hash: str
    nonce: str
    name: str
    picture: str
    given_name: str
    family_name: str
    iat: int
    exp: int

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _iss = str(obj.get("iss"))
        _azp = str(obj.get("azp"))
        _aud = str(obj.get("aud"))
        _sub = str(obj.get("sub"))
        _hd = str(obj.get("hd"))
        _email = str(obj.get("email"))
        _email_verified = str(obj.get("email_verified"))
        _at_hash = str(obj.get("at_hash"))
        _nonce = str(obj.get("nonce"))
        _name = str(obj.get("name"))
        _picture = str(obj.get("picture"))
        _given_name = str(obj.get("given_name"))
        _family_name = str(obj.get("family_name"))
        _iat = int(obj.get("iat"))
        _exp = int(obj.get("exp"))
        return Root(_iss, _azp, _aud, _sub, _hd, _email, _email_verified, _at_hash, _nonce, _name, _picture, _given_name, _family_name, _iat, _exp)