from django.urls import path
from . import views



urlpatterns = [
    path('', views.down),
    path('download/',views.yt_down),
]
