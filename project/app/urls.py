from django.urls import path
from . import views

urlpatterns = [
    path("sign-up", views.SignUpView.as_view(), name="sign-up"),
    path("usersign-up", views.ProfileSignUpView.as_view(), name="sign-up"),
    path("login", views.LoginView.as_view(), name="login"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("admin", views.AdminAccessView.as_view(), name="admin_login"),
    path("updateProfile/<str:pk>", views.UpdateProfileView.as_view(), name="admin_profile_update"),
    path("admin-createuser", views.AdminAddUserView.as_view(), name="admin-create-user"),
    path("manager-createuser", views.ManagerAddUserView.as_view(), name="manager-createuser"),
    path("admin-createuserprofile", views.AdminAddProfile.as_view(), name="admin-create-userprofile"),
    path("manager-createuserprofile", views.ManagerAddProfile.as_view(), name="manager-createuserprofile"),
]
