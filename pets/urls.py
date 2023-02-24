from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="List Pets"),
    path("create/", views.create, name="Create Pet"),
    path("edit/<int:id>/", views.edit, name="Edit/Update Pet"),
]
