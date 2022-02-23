from django.urls import path, include
from .views import home, latestImage

urlpatterns = [
    path("", home, name='home'),
    path('lastest', latestImage, name="latestImage"),
]
