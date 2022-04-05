
   
from django.urls import path, include

from .views import *

urlpatterns = [
    path('getRoles/', GetRolesView.as_view(), name='get_roles'),
]