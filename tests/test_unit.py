"""Behavioral unit tests for intake rules and service permissions."""

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.exceptions import PermissionDenied, ValidationError

from tickets.models import Ticket
from tickets.services import create_ticket, validate_ticket


@pytest.fixture
def payload():
    return {
        "title": "Printer fails",
        "description": "Cannot print a test page.",
        "category": "Hardware",
        "impact": "One user",
    }


def test_inclusive_text_bounds_and_whitespace(payload):
    payload["title"] = " " + "A" * 120 + " "
    payload["description"] = "B" * 4000
    result = validate_ticket(payload)
    assert result["title"] == "A" * 120
    assert result["description"] == "B" * 4000


@pytest.mark.parametrize("title", ["", " ", "X" * 121, 14])
def test_invalid_titles_are_rejected(payload, title):
    payload["title"] = title
    with pytest.raises(ValidationError):
        validate_ticket(payload)


@pytest.mark.parametrize("description", ["", "  ", "Y" * 4001, None])
def test_invalid_descriptions_are_rejected(payload, description):
    payload["description"] = description
    with pytest.raises(ValidationError):
        validate_ticket(payload)


@pytest.mark.parametrize("category", ["Hardware", "Software", "Network", "Access", "Other"])
def test_all_specified_categories_are_accepted(payload, category):
    payload["category"] = category
    assert validate_ticket(payload)["category"] == category


@pytest.mark.parametrize("impact", ["One user", "Multiple users", "Organization-wide"])
def test_all_specified_impacts_are_accepted(payload, impact):
    payload["impact"] = impact
    assert validate_ticket(payload)["impact"] == impact


@pytest.mark.parametrize(
    ("field", "value"),
    [("category", "Billing"), ("impact", "Worldwide"), ("category", []), ("impact", None)],
)
def test_unknown_or_nontyped_choices_rejected(payload, field, value):
    payload[field] = value
    with pytest.raises(ValidationError):
        validate_ticket(payload)


def test_client_cannot_set_state_or_owner(payload):
    payload["state"] = "Closed"
    with pytest.raises(ValidationError):
        validate_ticket(payload)


@pytest.mark.django_db
def test_identical_titles_create_distinct_tickets(payload):
    user = get_user_model().objects.create_user(username="user")
    user.groups.add(Group.objects.create(name="Requester"))
    first = create_ticket(user, payload)
    second = create_ticket(user, payload)
    assert first.pk != second.pk
    assert first.requester_id == second.requester_id == user.pk
    assert first.state == second.state == "New"


@pytest.mark.django_db
def test_invalid_payload_creates_no_partial_record(payload):
    user = get_user_model().objects.create_user(username="user")
    user.groups.add(Group.objects.create(name="Requester"))
    payload["description"] = " "
    with pytest.raises(ValidationError):
        create_ticket(user, payload)
    assert Ticket.objects.count() == 0


@pytest.mark.django_db
@pytest.mark.parametrize("role", ["Support", "Developer", "Administrator"])
def test_staff_roles_cannot_create_tickets(payload, role):
    user = get_user_model().objects.create_user(username="staff")
    user.groups.add(Group.objects.create(name=role))
    with pytest.raises(PermissionDenied):
        create_ticket(user, payload)
    assert Ticket.objects.count() == 0


@pytest.mark.django_db
def test_disabled_requester_cannot_create_ticket(payload):
    user = get_user_model().objects.create_user(username="disabled", is_active=False)
    user.groups.add(Group.objects.create(name="Requester"))
    with pytest.raises(PermissionDenied):
        create_ticket(user, payload)
    assert Ticket.objects.count() == 0
