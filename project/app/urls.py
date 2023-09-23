from django.urls import path
from . import views

urlpatterns = [
    path("sign-up", views.SignUpView.as_view(), name="sign-up"),
    path("usersign-up", views.ProfileSignUpView.as_view(), name="sign-up"),
    path("login", views.LoginView.as_view(), name="login"),
    path("profile", views.ProfileView.as_view(), name="login"),
    path("update-user", views.UpdateProfileView.as_view(), name="update"),



]
