from django.urls import path,include
from .views import LogInView,LogOutView,SignUpView,depositView,UserUpdateView,updateUserProfile

urlpatterns=[
    path('login/',LogInView.as_view(),name="login"),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('logout/',LogOutView.as_view(),name='logout'),
    path('update-profile',UserUpdateView.as_view(),name='update-profile'),
    path('deposit/',depositView,name='deposit'),
    path('update-user-profile',updateUserProfile,name='update-user-profile')
]