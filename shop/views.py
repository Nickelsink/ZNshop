from django.shortcuts import render
from shop.models import Goods, News


# Create your views here.


def main_view(request):
    goods = Goods.objects.all()
    return render(request, 'main.html', {'goods': goods})


def news(request):
    novosti = News.objects.All()
    args = {
        'novosti': novosti
    }
    return render(request, 'novosti.html', args)