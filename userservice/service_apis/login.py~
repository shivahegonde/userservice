from datetime import datetime

import django;

from userservice.utilities.get_dict import get_login_dict

django.setup()
from userservice.db.user_models.models import User as users
from userservice.db.user_models.models import Login as logins
from flask import jsonify, request
from flask_restful import Resource


def login(usersname, password):
    user = users.objects.get(username=usersname, password=password)
    # return True,user
    if user.username == usersname:
        return True


class Logins(Resource):
    def get(self, token=None):
        print(request.headers.get('User-Agent'))
        if token:
            loginuser = logins.objects.filter(token=token, is_active=True)[0]

            user_login_dict = get_login_dict(loginuser)
            for i in user_login_dict:
                print i, "  :  ", user_login_dict[i]
            return jsonify({"user": user_login_dict})

        allusers = logins.objects.all()
        user_login_list = [get_login_dict(x) for x in allusers]

        return ({"login ": user_login_list})

    def post(self   ):
        data = request.get_json()
        status = login(data['username'], data['password'])
        user = users.objects.get(username=data['username'])

        if status == True:

            login_entry = logins.objects.create(user=user,device_id=request.headers.get('User-Agent'))
            login_dict = get_login_dict(login_entry)
            return jsonify({"loginSuccess": login_dict})
        else:
            return jsonify({"message": "Invalid User"})

        # return jsonify({"users ": user_dict})

    def put(self, token):
        data = request.get_json()
        if token:
            logindata = logins.objects.get(token=token)
            logindata.is_active = False
            logindata.logout_time=datetime.now()
            logindata.save()
            login_dict = get_login_dict(logindata)
            return jsonify({"User: ": login_dict})

    def delete(self):
        data = request.get_json()
        user = users.objects.filter(username=data['username']).delete()
        # print "value: ",users.phone;
        user_dict = {"Name ": data['username'] + " deleted"}
        return jsonify({"User: ": user_dict})
