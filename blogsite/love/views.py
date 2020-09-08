from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, "love.html")

def marry(request):

    return render(request, "wedding.html")
