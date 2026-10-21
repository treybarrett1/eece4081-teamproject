"""Persisted ticket records belonging to authenticated requesters."""

from django.conf import settings
from django.db import models


class Ticket(models.Model):
    class Category(models.TextChoices):
        HARDWARE = "Hardware"
        SOFTWARE = "Software"
        NETWORK = "Network"
        ACCESS = "Access"
        OTHER = "Other"

    class Impact(models.TextChoices):
        ONE_USER = "One user"
        MULTIPLE_USERS = "Multiple users"
        ORGANIZATION_WIDE = "Organization-wide"

    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="support_tickets"
    )
    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=16, choices=Category.choices)
    impact = models.CharField(max_length=24, choices=Impact.choices)
    state = models.CharField(max_length=20, default="New", editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
