from fastapi import APIRouter, Depends, status, Body
from fastapi.responses import RedirectResponse
from fastapi.responses import JSONResponse
from auth.oauth2 import oauth2 as oauth
from Models.Auth import Root
from sqleditor import Sql, Tables
from auth.auth_handler import signJWT

class GoogleControllers():
    router = APIRouter()

    @router.route('/login')
    async def login(request):
        redirect_uri = request.url_for('auth')
        return await oauth.google.authorize_redirect(request, str(redirect_uri))


    @router.route('/auth')
    async def auth(request):
        token = await oauth.google.authorize_access_token(request)
        user = token.get('userinfo')
        if user:
            request.session['user'] = user
        users:Root = Root.from_dict(user)
        users_table = Sql().select_one_table(Tables.Person, users.email)
        if users.hd in ['mpt.ru','reu.ru'] and not users_table:
            data = {
                'Email': users.email,
                'Code': users.sub,
                'Surname': users.family_name,
                "Name": users.given_name,
                'Post': "Студент",
                'Image': users.picture
            }
            Sql().post(Tables.Person, data)
        users_table_one = Sql().select_one_table(Tables.Person, users.email)
        _url = 'http://127.0.0.1:8000'
        if not users_table_one:
            _url +='/private/'
            print('private')
        else:
            print('token')
            token = signJWT(users.email, users.sub,users.family_name,users.given_name,users.picture)
            _url += '/private/google_responce?key='+token
        request.session.pop('user', None)
        return RedirectResponse(_url)