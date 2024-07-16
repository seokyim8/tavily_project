from django.urls import path, include
from .views import generate

urlpatterns = [
    path("", generate),
]
