from django.shortcuts import render
#create your views here

def album(request):
    return render(request, "album.html", {})
