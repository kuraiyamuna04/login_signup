from django.urls import path
from . import views

urlpatterns = [
    path("sign-up", views.SignUpView.as_view(), name="sign-up"),
    path("usersign-up", views.ProfileSignUpView.as_view(), name="sign-up"),
    path("login", views.LoginView.as_view(), name="login"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("admin", views.AdminAccessView.as_view(), name="admin_login"),
    path("updateProfile/<str:pk>", views.UpdateProfileView.as_view(), name="admin_profile_update"),
    path("createuser", views.AddUserView.as_view(), name="admin-create-user"),
    path("createuserprofile", views.AddProfile.as_view(), name="manager-createuserprofile")
 ]
