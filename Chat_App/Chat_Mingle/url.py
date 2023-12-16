from django.urls import path
from . import views

urlpatterns = [


    # SignUp, Login, Logout
    path('',views.base,name='base'),
    path('register/',views.sign_up,name='sign_up'),
    path('login/',views.login_view,name='login'),
    path('chit_chat/',views.chit_chat,name='chit_chat'),
    path('room/',views.rooms_list,name='rooms_list'),
    path('chat/<str:room_name>/', views.room, name="chat"),

    ]
