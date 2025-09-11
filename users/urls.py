from django.urls import path,include
from .views import LogInView,LogOutView,SignUpView
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('login/',LogInView.as_view(),name="login"),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('logout/',LogOutView.as_view(),name='logout')
]