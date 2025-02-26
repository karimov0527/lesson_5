from django.urls import path,include
from .views import *


urlpatterns = [
    path('',home),
    path('smartphones/',include('smartphone.urls'))
]