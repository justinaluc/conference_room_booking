from django.shortcuts import render
from django.views.generic.list import ListView

# Create your views here.
from room_manager.models import ConferenceRoom


def home_page(request):
    return render(request, 'room_manager/base.html')


class RoomListView(ListView):

    model = ConferenceRoom
    paginate_by = 12
