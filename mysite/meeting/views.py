from pages.models import Event
from django.views import View
from .forms import CreateMeetingForm
from django.shortcuts import render, redirect

class CreateMeetingView(View):

    def get(self, request, *args, **kwargs):
        form = CreateMeetingForm()
        return render(request, 'form.html', {'form': form, 'title': 'Create Meeting'})

    def post(self, request, *args, **kwargs):
        form = CreateMeetingForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            event = Event(host = request.user, **form.cleaned_data)
            event.save()
            return redirect(f'/meet/{event.id}')
        else:
            return render(request, 'message.html', {'title': 'Failure', 'message': 'Failed to create a new event.'})


class MeetingView(View):
    def get(self, request, event_id, *args, **kwargs):
        event = Event.objects.get(pk=event_id)
        return render(request, 'event.html', {'event': event})

class JoinMeetingView(View):
    def post(self, request, event_id, *args, **kwargs):
        event = Event.objects.get(pk=event_id)
        if request.user.is_authenticated:
            event.attendees.add(request.user)
        else:
            pass
    def delete(self, request, event_id, *args, **kwargs):
        event = Event.objects.get(pk=event_id)
        if request.user.is_authenticated:
            event.attendees.remove(request.user)
        else:
            pass

class EditMeetingView(View):
    def get(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        form = CreateMeetingForm(instance=event)
        return render(request, 'form.html', {'form': form, 'title': 'Edit Meeting'})
    def post(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        form = CreateMeetingForm(request.POST, instance=event)
        if request.user.is_authenticated and form.is_valid() and event.host == request.user:
            form.save()
            return redirect(f'/meet/{event.id}')
        else:
            return render(request, 'message.html', {'title': 'Failure', 'message': 'Failed to edit existing event.'})
