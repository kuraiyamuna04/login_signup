from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview,name='apiOverview' ),
    path("task-list",views.taskList,name="taskview"),
    path("task-detail/<str:pk>",views.viewone, name="viewone"),
    path("task-update/<str:pk>", views.update, name="update")

]
