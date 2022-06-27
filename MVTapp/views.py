from django.http import HttpResponse
from django.shortcuts import render

from MVTapp.models import familia

# Create your views here.


def mi_vista(request):
     return HttpResponse('<h1>Hola, esta es mi familia</h1>')


def nueva_vista(request):

     familia1=familia(nombre='Ana',edad='65',fecha_de_nacimiento='1957-6-29')
     familia2=familia(nombre='Pedro',edad='62',fecha_de_nacimiento='1960-10-30')
     familia3=familia(nombre='Pepito',edad='32',fecha_de_nacimiento='1990-2-23')

     familia1.save()
     familia2.save()
     familia3.save()

     lista_familia1 = familia.objects.all()

     return render(request,'index.html',{'lista_de_objetos':[familia1,familia2,familia3]}) 