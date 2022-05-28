from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {
        'name': 'Jalloh',
        'age': 99,
        'nationality': 'African'
    }
    return render(request, 'index.html', context)
