from django.urls import path
# this imports views/py from current directory
from . import views

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
]