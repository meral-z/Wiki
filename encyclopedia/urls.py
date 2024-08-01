from django.urls import path

from . import views

app_name= "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>/", views.entry, name="entry"),
    path("random/",views.random_entry, name="random_entry"),
]
