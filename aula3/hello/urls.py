from django.urls import path
from . import views # . means current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("matheus/", views.matheus, name="matheus"),
    path("greet/<str:name>/", views.greet, name="greet"),
]
