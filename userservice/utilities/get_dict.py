from userservice.service_apis.user import get_user_dict


def get_login_dict(login):
    return  {"loginTime": str(login.login_time),"logout_time": str(login.logout_time), "token": str(login.token),
            "is_active": login.is_active, "device_id": login.device_id, "user": get_user_dict(login.user)}
