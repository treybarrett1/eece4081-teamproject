"""HTTP acceptance: actual session, CSRF, database, and two-user access boundary."""

import json

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import Client

from tickets.models import Ticket


@pytest.fixture
def users(db):
    result = {}
    for name, role in (
        ("requester_a", "Requester"),
        ("requester_b", "Requester"),
        ("support_a", "Support"),
        ("developer_a", "Developer"),
    ):
        user = get_user_model().objects.create_user(
            username=name, password="synthetic-only-password"
        )
        user.groups.add(Group.objects.get_or_create(name=role)[0])
        result[name] = user
    return result


def call(client, method, path, payload):
    return getattr(client, method)(
        path,
        data=json.dumps(payload),
        content_type="application/json",
        HTTP_X_CSRFTOKEN=client.cookies["csrftoken"].value,
    )


def sign_in(client, username):
    client.get("/api/csrf/")
    return call(
        client,
        "post",
        "/api/session/",
        {"username": username, "password": "synthetic-only-password"},
    )


@pytest.mark.django_db
def test_session_to_creation_to_visible_own_ticket_with_isolation(users):
    """Use the full HTTP boundary, and verify a persisted, attributed ticket."""
    alice = Client(enforce_csrf_checks=True)
    assert sign_in(alice, "requester_a").status_code == 200
    created = call(
        alice,
        "post",
        "/api/tickets/",
        {
            "title": "T" * 120,
            "description": "Laptop will not connect.",
            "category": "Network",
            "impact": "One user",
        },
    )
    assert created.status_code == 201
    ticket_id = created.json()["id"]
    stored = Ticket.objects.get(pk=ticket_id)
    assert stored.requester_id == users["requester_a"].pk
    assert created.json()["state"] == "New"
    assert created.json()["priority"] is None
    assert alice.get(f"/api/tickets/{ticket_id}/").json()["title"] == "T" * 120
    assert [t["id"] for t in alice.get("/api/tickets/").json()["tickets"]] == [
        ticket_id
    ]

    bob = Client(enforce_csrf_checks=True)
    assert sign_in(bob, "requester_b").status_code == 200
    assert bob.get(f"/api/tickets/{ticket_id}/").status_code == 404
    assert bob.get("/api/tickets/").json()["tickets"] == []

    staff = Client(enforce_csrf_checks=True)
    assert sign_in(staff, "support_a").status_code == 200
    assert staff.get(f"/api/tickets/{ticket_id}/").status_code == 200

    assert call(alice, "delete", "/api/session/", {}).status_code == 200
    assert alice.get("/api/tickets/").status_code == 401


@pytest.mark.django_db
def test_forged_requester_id_does_not_create_record(users):
    alice = Client(enforce_csrf_checks=True)
    assert sign_in(alice, "requester_a").status_code == 200
    result = call(
        alice,
        "post",
        "/api/tickets/",
        {
            "title": "Need help",
            "description": "Portal is down.",
            "category": "Access",
            "impact": "One user",
            "requester_id": users["requester_b"].pk,
        },
    )
    assert result.status_code == 400
    assert Ticket.objects.count() == 0


@pytest.mark.django_db
def test_csrf_logout_and_wrong_role_are_denied(users):
    anonymous = Client(enforce_csrf_checks=True)
    assert anonymous.get("/api/tickets/").status_code == 401
    assert (
        anonymous.post(
            "/api/session/", data="{}", content_type="application/json"
        ).status_code
        == 403
    )
    developer = Client(enforce_csrf_checks=True)
    assert sign_in(developer, "developer_a").status_code == 200
    assert developer.get("/api/tickets/").status_code == 403
    assert Ticket.objects.count() == 0
