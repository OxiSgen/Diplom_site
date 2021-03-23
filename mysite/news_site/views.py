# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .modules.Paeser import main as Pars
from .forms import ContactForm
from django.http import JsonResponse
import schedule
import time
from .models import News


class news1(generic.ListView):
    """news = Pars()
    for n in news:
        s = News(news_text=n[1], news_url=n[0], news_hype_rate=n[2])
        s.save()"""
    """ if request.method == "POST" and request.is_ajax():
        form = ContactForm(request.POST)
        form.save()
        return JsonResponse({"success": True}, status=200)
    return render(request, 'base.html') """
    # news = News

    def get_queryset(self):
        return News.objects.filter(news_hype_rate__lte=5)


class news2(generic.ListView):
    news = News

    def get_queryset(self):
        return News.objects.filter(news_hype_rate__range=(6, 20))


class news3(generic.ListView):
    news = News

    def get_queryset(self):
        return News.objects.filter(news_hype_rate__range=(21, 100))

class news4(generic.ListView):
    news = News

    def get_queryset(self):
        return News.objects.filter(news_hype_rate__range=(101, 200))

class news5(generic.ListView):
    news = News

    def get_queryset(self):
        return News.objects.filter(news_hype_rate__range=(201, 1000))

class news6(generic.ListView):
    news = News

    def get_queryset(self):
        return News.objects.filter(news_hype_rate__gt=1000)

class news7(generic.ListView):
    news = News

    def get_queryset(self):
        return News.objects.all()