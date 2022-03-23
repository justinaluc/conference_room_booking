from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView

# Create your views here.
from room_manager.models import ConferenceRoom


def home_page(request):
    return render(request, 'room_manager/base.html')


class RoomListView(ListView):

    model = ConferenceRoom
    paginate_by = 12
    context_object_name = 'list_of_all_rooms_in_database'
    template_name = 'room_manager/conferenceroom_list.html'


class RoomDetailView(DetailView):

    model = ConferenceRoom


class AddRoomView(CreateView):

    model = ConferenceRoom
    fields = ['name', 'capacity', 'projector']
    context_object_name = 'add_new_room_to_database'

    def get_success_url(self):
        return reverse('room_list',)