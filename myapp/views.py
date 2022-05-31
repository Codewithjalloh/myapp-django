from django.shortcuts import render
from django.http import HttpResponse
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
