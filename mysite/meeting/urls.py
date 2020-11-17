from .views import CreateMeetingView, MeetingView, JoinMeetingView, EditMeetingView
from django.urls import path

urlpatterns = [
    path('create/', CreateMeetingView.as_view()),
    path('<int:event_id>/', MeetingView.as_view()),
    path('<int:event_id>/join/', JoinMeetingView.as_view()),
    path('<int:event_id>/edit/', EditMeetingView.as_view()),
]