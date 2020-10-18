from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>", views.title, name="title"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new_page"),
    path("check_new", views.check_new, name="check_new"),
    path("editing/<heading>", views.editing, name="editing"),
    path("random_page", views.random_page, name="random_page"),
]
