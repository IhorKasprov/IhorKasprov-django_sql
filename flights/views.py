from django.shortcuts import render
from .models import Flight

# Створюємо наші views.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
        })