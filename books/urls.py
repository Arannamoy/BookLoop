from django.urls import path
from .views import getSpecificBook,borrowBook,returnBook,getAllBook

urlpatterns=[
    path("all-book/<slug:slug>",getAllBook,name="get-all-book"),
    path("<int:id>",getSpecificBook,name="specific_book"),
    path("borrow/<int:id>",borrowBook,name="borrow_book"),
    path("return/<int:book_id>/<int:borrow_id>",returnBook,name="return_book")
]