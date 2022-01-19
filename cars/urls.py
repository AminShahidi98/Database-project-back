from django.urls import path
from . import views

urlpatterns = [
    path("show-person-cars/<str:NID>/", views.showPersonCars, name="show person cars"),
    path("find-person-cars/", views.findPersonCars, name="find person cars"),
    path("debtor-list-dec/", views.debtorCars, name="debtor cars list dec"),
]