from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.register, name="signup"),
    path("login/", views.staff_login, name="login"),
    path("home/", views.home, name="home"),
    path("staff-dashboard/", views.staff_dashboard, name="staff-dashboard"),
]