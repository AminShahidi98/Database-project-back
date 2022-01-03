from django.urls import path
from . import views

urlpatterns = [
    path("<int:CID>/servicemans/", views.cameraServicemans, name="camera servicemans"),
    path("servicemans/find/", views.findCameraServicemans, name="find camera servicemans"),
    path("costs-list-asc/", views.camerasCostsAsc, name="cameras costs asc"),
    path("costs-list-dec/", views.camerasCostsDec, name="cameras costs dec")
]