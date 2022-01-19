from django.urls import path
from . import views

urlpatterns = [
    path("show-receipts/<str:FID>/", views.showReceipts, name="show receipt of a fine"),
    path("find-receipts/", views.findReceipts, name="find receipt of a fine"),
]