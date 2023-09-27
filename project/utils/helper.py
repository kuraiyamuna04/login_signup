from app.models import CustomUser


def check_post_req_role(user_id):
    user = CustomUser.objects.get(id=user_id)
    role = user.role
    if role != "E":
        return False
    return True



