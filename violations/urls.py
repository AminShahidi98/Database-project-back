from django.urls import path
from . import views

urlpatterns = [
    path("list-asc/", views.showViolationsListAsc, name="show violations list asc"),
    path("list-dec/", views.showViolationsListDec, name="show violations list dec"),
]