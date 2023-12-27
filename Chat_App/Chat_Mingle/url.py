from django.urls import path
from . import views

urlpatterns = [


    # SignUp, Login, Logout
    path('',views.base,name='base'),
    path('register/',views.sign_up,name='sign_up'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('chit_chat/',views.user_profile,name='chit_chat'),
    path('room/',views.enter_room,name='enter_room'),
    path('chat/<str:room_name>/', views.room, name="chat"),
    ]
