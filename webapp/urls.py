from webapp import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("single", views.single_viewer, name="single"),
    path("dynamic", views.dynamic_viewer, name="dynamic"),
]