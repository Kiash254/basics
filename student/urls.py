from django.urls import path 
from student import views
from student.views import RoomDetail, RoomUpdateView, RoomDeleteView

app_name='student'

urlpatterns=[
    path("",views.home,name="home"),
    path("room/",views.room,name="room"),
    path("room/<int:pk>/", RoomDetail, name='room-detail'),
    path('room/<int:pk>/update', RoomUpdateView, name='room-update'),
    path('room/<int:pk>/delete', RoomDeleteView, name='room-delete'),
    # path("create-room/",views.createroom,name="create-room"),
    path("create-room/",views.Createroom, name="create-room"),

]