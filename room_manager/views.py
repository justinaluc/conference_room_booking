import datetime

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.views.generic.list import ListView

from room_manager.models import ConferenceRoom, ReserveRoom


def home_page(request):
    return render(request, 'room_manager/base.html')


class RoomListView(ListView):

    model = ConferenceRoom
    paginate_by = 12
    context_object_name = 'list_of_all_rooms_in_database'
    template_name = 'room_manager/conferenceroom_list.html'
    ordering = ['name']


class RoomDetailView(DetailView):

    model = ConferenceRoom

    def get(self, request, pk):
        room = ConferenceRoom.objects.get(id=pk)
        reservations = room.reserveroom_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, "room_manager/conferenceroom_detail.html", context={"room": room, "reservations": reservations})


class RoomAddView(CreateView):

    model = ConferenceRoom
    fields = ['name', 'capacity', 'projector']
    context_object_name = 'add_new_room_to_database'

    def get_success_url(self):
        return reverse('room_list',)


class RoomUpdateView(UpdateView):
    model = ConferenceRoom
    fields = ['name', 'capacity', 'projector']
    context_object_name = 'edit_existing_room_in_database'

    def get_success_url(self):
        return reverse('room_list',)


class RoomDeleteView(DeleteView):

    model = ConferenceRoom

    def get_success_url(self):
        return reverse('room_list',)


class ReservationView(View):

    def get(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        return render(request, "room_manager/reserveroom_detail.html", context={"room": room})

    def post(self, request, room_id):
        room = ConferenceRoom.objects.get(id=room_id)
        date = request.POST.get("reservation-date")
        comment = request.POST.get("comment")

        if ReserveRoom.objects.filter(room_id=room, date=date):
            return render(request, "room_manager/reserveroom_detail.html",
                          context={"room": room, "error": f"Conference Room already reserved for this date! ({date})"})
        if date < str(datetime.date.today()):
            return render(request, "room_manager/reserveroom_detail.html",
                          context={"room": room, "error": "Date is from the past! You have to choose the future date."})

        ReserveRoom.objects.create(room_id=room, date=date, comment=comment)
        return redirect("room_list")
