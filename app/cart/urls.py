from django.urls import path, include
from django.conf import settings
from .views import *


urlpatterns = [
    path('addCart/<int:id>/', cart_add, name="add_cart"),


] 