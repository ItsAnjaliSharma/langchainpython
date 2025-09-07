from django.urls import path
from chef.views import Home

urlpatterns=[
    path('', Home.as_view(), name='home')
]