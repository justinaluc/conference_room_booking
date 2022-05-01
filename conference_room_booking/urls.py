"""conference_room_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from room_manager.views import (
    home_page,
    RoomListView,
    RoomDetailView,
    RoomUpdateView,
    RoomDeleteView,
    RoomAddView,
    ReservationView,
    SearchView
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('room/', RoomListView.as_view(), name="room_list"),
    path('room/<int:pk>', RoomDetailView.as_view(), name="room_detail"),
    path('room/delete/<int:pk>', RoomDeleteView.as_view(), name="room_delete"),
    path('room/modify/<int:pk>', RoomUpdateView.as_view(), name="room_update"),
    path('room/reserve/<int:room_id>', ReservationView.as_view(), name="room_reserve"),
    path('room/new', RoomAddView.as_view(), name="room_add"),
    path('search_room/', SearchView.as_view(), name="search_room"),
]
