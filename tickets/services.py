"""Ticket creation rules with documented inclusive input limits."""

from django.core.exceptions import PermissionDenied, ValidationError

from tickets.models import Ticket

INPUT_FIELDS = {"title", "description", "category", "impact"}


def has_role(user, role):
    return (
        user.is_authenticated
        and user.is_active
        and user.groups.filter(name=role).exists()
    )


def validate_ticket(payload):
    """Only public intake fields are accepted; whitespace is trimmed."""
    if not isinstance(payload, dict) or set(payload) != INPUT_FIELDS:
        raise ValidationError("Exactly four ticket intake fields are required.")
    result = {}
    for field, limit in (("title", 120), ("description", 4000)):
        value = payload[field]
        if not isinstance(value, str):
            raise ValidationError({field: "Must be text."})
        value = value.strip()
        if not value or len(value) > limit:
            raise ValidationError({field: "Blank or longer than allowed."})
        result[field] = value
    for field, allowed in (
        ("category", set(Ticket.Category.values)),
        ("impact", set(Ticket.Impact.values)),
    ):
        value = payload[field]
        if not isinstance(value, str) or value not in allowed:
            raise ValidationError({field: "Invalid choice."})
        result[field] = value
    return result


def create_ticket(user, payload):
    """The authenticated user owns the ticket; client IDs are never trusted."""
    if not has_role(user, "Requester"):
        raise PermissionDenied("Only an active Requester can create a ticket.")
    return Ticket.objects.create(requester=user, **validate_ticket(payload))
