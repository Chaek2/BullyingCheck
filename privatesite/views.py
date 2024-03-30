from django.shortcuts import render,redirect
from django.http import HttpResponse
import api
import jwt

_key='nRfzgTAOMtwaW9ezqnzNyzG5LAfBYcPDRHzSiwtkePin'

def profile(request):
    try:
        id = request.COOKIES["GoogleID"]
        tokens(id)
        if not (not id):
            app = api.get_all(api.Tables.Application)
            data = {
                'google':id,
                'app':app
            }
            return render(request, 'privatesite/profile.html',context= data)
    except Exception as ex:
        print(ex, 69)
        return render(request, 'privatesite/profile.html')


def google_responce(request):
    responce = redirect('profile')
    responce.set_cookie('GoogleID',request.GET['key'])
    return responce

def tokens(token: str):
    try:
        res = jwt.decode(token, key=_key, algorithms=['HS256', ],audience='REYS_')
        item:api.Tokens = api.Tokens(res)
        listperson = api.get_one(api.Tables.Person,item.Email)
        if not listperson:
            datas ={
                "email": f'{item.Email}',
                "identifier": f'{item.Identifier}',
                "surname": f'{item.Surname}',
                "name": f'{item.Name}',
                "post": "Студент",
                "image": f'{item.Picture}',
            }
            resp = api.post_all(api.Tables.Person,datas,token)
            print(resp, 201)
    except Exception as e:        
        print(e, 48)