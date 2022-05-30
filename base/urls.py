from django.urls import path
from base import views

urlpatterns = [
    path("", views.home, name="home"),
    path("certifications", views.all_certifications, name= "all_certifications"),
    path("contact/<str:message>", views.contact, name="contact")
]

