from django.urls import path
# this imports views/py from current directory
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart')
]
