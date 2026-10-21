"""Routes exercised by the HTTP acceptance tests."""

from django.urls import path

from tickets.views import csrf_token, session, ticket_detail, tickets

urlpatterns = [
    path("api/csrf/", csrf_token),
    path("api/session/", session),
    path("api/tickets/", tickets),
    path("api/tickets/<int:ticket_id>/", ticket_detail),
]
