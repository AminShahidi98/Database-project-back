from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup/", views.register, name="signup"),
    path("citizen-signup/", views.citizen_register, name="citizen-signup"),
    path("login/", views.staff_login, name="login"),
    path("citizen-login/", views.citizen_login, name="citizen-login"),
    path("home/", views.home, name="home"),
    path("staff-dashboard/", views.staff_dashboard, name="staff-dashboard"),
    path("citizen-dashboard/", views.citizen_dashboard, name="citizen-dashboard"),
]