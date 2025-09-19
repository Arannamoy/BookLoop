from django.urls import path
from .views import getSpecificBook

urlpatterns=[
    # path("all",getAllBook,name="home"),
    path("<int:id>",getSpecificBook,name="specific_book")
]