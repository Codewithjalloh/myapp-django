import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature


# Create your views here.


def index(request):
    # context = {
    #     'name': 'Jalloh',
    #     'age': 99,
    #     'nationality': 'African'
    # }
    # feature1 = Feature()
    # feature1.id = 1
    # feature1.name = 'Fast'
    # feature1.is_true = True
    # feature1.details = 'Out service is very fast'

    # feature2 = Feature()
    # feature2.id = 2
    # feature2.name = 'quick'
    # feature2.is_true = True
    # feature2.details = 'Out service is very quick'

    # feature3 = Feature()
    # feature3.id = 3
    # feature3.name = 'affordable '
    # feature3.is_true = False
    # feature3.details = 'Out service is very affordable'

    # feature4 = Feature()
    # feature4.id = 4
    # feature4.name = 'easy to use '
    # feature4.is_true = True
    # feature4.details = 'Out service is very easy of use'

    # feature5 = Feature()
    # feature5.id = 4
    # feature5.is_true = False
    # feature5.name = 'TrustWorthy '
    # feature5.details = 'Out service is very trustworthy'

    # features = [feature1, feature2, feature3, feature4, feature5]
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')
