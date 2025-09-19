from django.urls import path
from .views import read
urlpatterns=[
    # path('create/',create,name=create),
    path('read/',read,name='read')
    
]