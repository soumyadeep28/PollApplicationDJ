from unicodedata import name
from django.urls import path
from main import views

urlpatterns=[
    path('', views.Index.as_view() , name = 'index'),
    path('questions/<slug>' , views.Details.as_view() , name='questions')
]

# you can also use this path('questions/<int:pk>' , views.Details.as_view() , name='questions')