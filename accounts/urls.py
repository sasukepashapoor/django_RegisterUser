from django.urls import path
from .views import  register_user

urlpatterns =[
    path ('register_user/',register_user.as_view() )
]

