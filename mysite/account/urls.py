from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up', sign_up),
    path('sign_in', sign_in),
    path('sign_out', sign_out),
    path('profile', profile),
    path('ajax_reg1', ajax_reg1),
    path('ajax_reg2', ajax_reg2),
]