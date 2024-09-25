from django.urls import path
from v1.views import main

urlpatterns = [
    path('test/', main),
]
