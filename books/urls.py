from django.urls import path
from .views import getSpecificBook,borrowBook

urlpatterns=[
    # path("all",getAllBook,name="home"),
    path("<int:id>",getSpecificBook,name="specific_book"),
    path("<int:id>",borrowBook,name="borrow_book")
]