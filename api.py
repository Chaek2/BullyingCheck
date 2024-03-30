import requests
import json
from enum import Enum

_url = 'http://localhost:5062/api/'


class Tokens:
    Identifier: str
    FullName: str
    Name: str
    Surname: str
    Email: str
    Picture: str

    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])


class Tables(Enum):
    Category = 'Category'
    Tag = 'Tag'
    Post = 'Post'
    Relese = 'Relese'
    Person = 'Person'
    Application = 'Application'
    Category_App = 'CategoryApp'
    Tag_App = 'TagApp'
    Relese_App = 'ReleseApp'
    Raiting = 'Raiting'
    Feedback = 'Feedback'


def get_all(tables: Tables):
    print('get_all', f"{_url+str(tables.value)}")
    response = requests.get(f"{_url+str(tables.value)}")
    if response.ok:
        return response.json()
    return None


def get_one(tables: Tables, id):
    print('get_one', f"{_url+str(tables.value)}/{id}")
    response = requests.get(f"{_url+str(tables.value)}/{id}")
    if response.ok:
        return response.json()
    return None


def post_all(tables: Tables, data, key: str):
    print('post', f"{_url+str(tables.value)}")
    response = requests.post(f"{_url+tables.value}",
                             headers={'Authorization': 'Bearer '+key},
                             json=data)
    if response.ok:
        return True
    return False


def put_all(tables: Tables, data, id, key: str):
    print('put', f"{_url+str(tables.value)}")
    response = requests.put(f"{_url+tables.value}/{id}",
                            headers={'Authorization': 'Bearer '+key},
                            json=data)
    if response.ok:
        return True
    return False


def delete_all(tables: Tables, id, key: str):
    print('delete', f"{_url+str(tables.value)}/{id}")
    response = requests.delete(f"{_url+tables.value}/{id}",
                               headers={'Authorization': 'Bearer '+key})
    if response.ok:
        return True
    return False
