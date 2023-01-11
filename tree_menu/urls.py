from django.urls import path
from . import views

urlpatterns = [
    path("<str:name>/", views.get_menu, name="menu_item"),
    path("", views.get_menu)
]
