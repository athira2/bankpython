from . import views
from django.urls import path
app_name='travelapp'
urlpatterns = [

    path('',views.demo,name='demo')
]
