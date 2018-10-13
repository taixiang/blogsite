from django.shortcuts import render
from .models import Msmm

# Create your views here.

def index(request):
    counts = Msmm.objects.get_or_create(id=1)[0]
    counts.count += 1
    counts.save()
    return render(request, "msmm.html")
