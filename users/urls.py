from django.urls import path
from .views import Home

app_name = 'users'
urlpatterns = [
    path('', Home.as_view(), name='homepage'),
]
