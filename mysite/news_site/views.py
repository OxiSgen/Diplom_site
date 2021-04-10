from django.shortcuts import render
from django.views import generic

from .models import News

from .charts import DemoChart

import pickle

user_interest = []

class News1(generic.ListView):
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

    def get(self, request):
        num_visits1 = request.session.get('num_visits1', 0)
        request.session['num_visits1'] = num_visits1 + 1
        news_l = News.objects.filter(news_hype_rate__lte=5)[::2]
        news_r = News.objects.filter(news_hype_rate__lte=5)[1::2]
        news_list = zip(news_l, news_r)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': news_list},
        )


class News2(generic.ListView):
    news = News

    def get(self, request):
        num_visits2 = request.session.get('num_visits2', 0)
        request.session['num_visits2'] = num_visits2 + 1
        news_l = News.objects.filter(news_hype_rate__range=(6, 20))[::2]
        news_r = News.objects.filter(news_hype_rate__range=(6, 20))[1::2]
        news_list = zip(news_l, news_r)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': news_list},
        )


class News3(generic.ListView):
    news = News

    def get(self, request):
        num_visits3 = request.session.get('num_visits3', 0)
        request.session['num_visits3'] = num_visits3 + 1
        news_l = News.objects.filter(news_hype_rate__range=(21, 100))[::2]
        news_r = News.objects.filter(news_hype_rate__range=(21, 100))[1::2]
        news_list = zip(news_l, news_r)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': news_list},
        )


class News4(generic.ListView):
    news = News

    def get(self, request):
        num_visits4 = request.session.get('num_visits4', 0)
        request.session['num_visits4'] = num_visits4 + 1
        news_l = News.objects.filter(news_hype_rate__range=(101, 200))[::2]
        news_r = News.objects.filter(news_hype_rate__range=(101, 200))[1::2]
        news_list = zip(news_l, news_r)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': news_list},
        )


class News5(generic.ListView):
    news = News

    def get(self, request):
        num_visits5 = request.session.get('num_visits5', 0)
        request.session['num_visits5'] = num_visits5 + 1
        news_l = News.objects.filter(news_hype_rate__range=(201, 1000))[::2]
        news_r = News.objects.filter(news_hype_rate__range=(201, 1000))[1::2]
        news_list = zip(news_l, news_r)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': news_list},
        )


class News6(generic.ListView):
    news = News

    def get(self, request):
        num_visits6 = request.session.get('num_visits6', 0)
        request.session['num_visits6'] = num_visits6 + 1
        news_l = News.objects.filter(news_hype_rate__gt=1000)[::2]
        news_r = News.objects.filter(news_hype_rate__gt=1000)[1::2]
        news_list = zip(news_l, news_r)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': news_list},
        )


class News7(generic.ListView):
    news = News

    def get(self, request):
        num_visits7 = request.session.get('num_visits7', 0)
        request.session['num_visits7'] = num_visits7 + 1
        news_l = News.objects.filter(news_hype_rate__gt=500)[::2]
        news_r = News.objects.filter(news_hype_rate__gt=500)[1::2]
        news_list = zip(news_l, news_r)
        return render(
            request,
            'news_site/news_list.html',
            {'object_list': news_list},
        )


class NewsIndividual(generic.TemplateView):
    template_name = 'news_site/individual.html'

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        num_visits8 = self.request.session.get('num_visits8', 0)
        self.request.session['num_visits8'] = num_visits8 + 1

        # self.request.session.flush()

        context = {
                      'chart': DemoChart(queryset=list(self.request.session.items())),
                      'num_visits': self.request.session.items(),  # num_visits appended
        }
        return context
