"""Initial ticket table."""

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]  # noqa: RUF012

    operations = [  # noqa: RUF012
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=120)),
                ("description", models.TextField()),
                (
                    "category",
                    models.CharField(
                        max_length=16,
                        choices=[
                            ("Hardware", "Hardware"),
                            ("Software", "Software"),
                            ("Network", "Network"),
                            ("Access", "Access"),
                            ("Other", "Other"),
                        ],
                    ),
                ),
                (
                    "impact",
                    models.CharField(
                        max_length=24,
                        choices=[
                            ("One user", "One User"),
                            ("Multiple users", "Multiple Users"),
                            ("Organization-wide", "Organization Wide"),
                        ],
                    ),
                ),
                (
                    "state",
                    models.CharField(max_length=20, default="New", editable=False),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "requester",
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="support_tickets",
                    ),
                ),
            ],
        )
    ]
