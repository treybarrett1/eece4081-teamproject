"""CSRF-protected JSON request boundary with session and role checks."""

import json

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied, ValidationError
from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_GET

from tickets.models import Ticket
from tickets.services import create_ticket, has_role


def parse_body(request):
    try:
        value = json.loads(request.body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise ValueError("Invalid JSON.") from None
    if not isinstance(value, dict):
        raise ValueError("A JSON object is required.")
    return value


def present(ticket):
    return {
        "id": ticket.pk,
        "title": ticket.title,
        "description": ticket.description,
        "category": ticket.category,
        "impact": ticket.impact,
        "state": ticket.state,
        "owner": None,
        "priority": None,
        "created_at": ticket.created_at.isoformat(),
    }


@ensure_csrf_cookie
@require_GET
def csrf_token(request):
    return JsonResponse({"ok": True})


def session(request):
    if request.method == "POST":
        try:
            credentials = parse_body(request)
        except ValueError:
            return JsonResponse({"error": "Invalid credentials."}, status=401)
        if set(credentials) != {"username", "password"}:
            return JsonResponse({"error": "Invalid credentials."}, status=401)
        user = authenticate(
            request,
            username=credentials["username"],
            password=credentials["password"],
        )
        if user is None or not (
            has_role(user, "Requester")
            or has_role(user, "Support")
            or has_role(user, "Developer")
            or has_role(user, "Administrator")
        ):
            return JsonResponse({"error": "Invalid credentials."}, status=401)
        login(request, user)
        return JsonResponse({"authenticated": True})
    if request.method == "DELETE":
        logout(request)
        return JsonResponse({"authenticated": False})
    return HttpResponseNotAllowed(["POST", "DELETE"])


def tickets(request):
    if not request.user.is_authenticated or not request.user.is_active:
        return JsonResponse({"error": "Authentication required."}, status=401)
    requester = has_role(request.user, "Requester")
    support = has_role(request.user, "Support")
    if not (requester or support):
        return JsonResponse({"error": "Forbidden."}, status=403)
    if request.method == "POST":
        if not requester:
            return JsonResponse({"error": "Forbidden."}, status=403)
        try:
            ticket = create_ticket(request.user, parse_body(request))
        except ValueError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)
        except ValidationError as exc:
            return JsonResponse({"error": exc.messages}, status=400)
        except PermissionDenied:
            return JsonResponse({"error": "Forbidden."}, status=403)
        return JsonResponse(present(ticket), status=201)
    if request.method == "GET":
        rows = Ticket.objects.order_by("pk")
        if requester:
            rows = rows.filter(requester=request.user)
        return JsonResponse({"tickets": [present(ticket) for ticket in rows]})
    return HttpResponseNotAllowed(["GET", "POST"])


@require_GET
def ticket_detail(request, ticket_id):
    if not request.user.is_authenticated or not request.user.is_active:
        return JsonResponse({"error": "Authentication required."}, status=401)
    if not (has_role(request.user, "Requester") or has_role(request.user, "Support")):
        return JsonResponse({"error": "Forbidden."}, status=403)
    rows = Ticket.objects.all()
    if has_role(request.user, "Requester"):
        rows = rows.filter(requester=request.user)
    try:
        ticket = rows.get(pk=ticket_id)
    except Ticket.DoesNotExist:
        raise Http404("No ticket.") from None
    return JsonResponse(present(ticket))
