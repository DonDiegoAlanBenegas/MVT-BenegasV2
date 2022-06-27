from django.urls import path
from .views import mi_vista,nueva_vista


urlpatterns = [

    path('',mi_vista),
    path('mi-template/',nueva_vista)
]