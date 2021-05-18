from django.urls import path
from .views import home, generate


urlpatterns = [
    path('', home, name='home'),
    path('generate/', generate, name='generate'),
]
