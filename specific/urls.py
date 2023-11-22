from specific.views import *
from django.urls import path

app_name='something'
urlpatterns=[
    path('three/',three,name='three'),
    path('four/',four, name='four'),
]
