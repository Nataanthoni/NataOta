from django.shortcuts import render

# Create your views here.
from .models import Booking


def index(request):
    return render(request, 'index.html')


def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')