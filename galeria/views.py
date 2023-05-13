from django.shortcuts import render
from galeria.models import Galeria

# Create your views here.
def galeria(request):
    galeria=Galeria.objects.all()
    return render(request, 'templates/galeria.html', {"galerias": galeria})
