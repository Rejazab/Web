from django.urls import path
from . import views

app_name = "back_end"
urlpatterns = [
	path("", views.index, name="index"),
	path("<str:language>/", views.global_information, name="informations"),
	path("<str:language>/AboutMe", views.about, name="about"),
	path("<str:language>/Formations", views.formations, name="formations"),
	path("<str:language>/Experiences", views.experiences, name="experiences"),
]
