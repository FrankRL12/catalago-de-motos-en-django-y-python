from django.urls import path
from galeria import views

urlpatterns = [
    path('', views.galeria, name='galeria'),
]
