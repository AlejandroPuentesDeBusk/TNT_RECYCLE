from django.shortcuts import render
from django.http import HttpResponse


# Aqui creamos cada funcion de render request para que renderice la viste que creeamos
def finanzas(request):
    return render(request, 'finanzas.html')
