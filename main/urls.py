from django.urls import path
from .views import index, site


urlpatterns = [
    path('', index, name='index'),
    path('<str:pk>/', site, name='site'),
]
