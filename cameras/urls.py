from django.urls import path
from . import views

urlpatterns = [
    path("<int:CID>/servicemans/", views.cameraServicemans, name="camera servicemans")
]