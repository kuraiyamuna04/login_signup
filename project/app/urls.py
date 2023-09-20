from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,name='apiOverview' ),
    path("sign-up",views.signUp,name="sign-up"),
    path("login",views.login, name="login"),


]
