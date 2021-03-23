from django.urls import path

from . import views

urlpatterns = [
    path('', views.news1.as_view(), name='news1'),
    path('news2/', views.news2.as_view(), name='news2'),
    path('news3/', views.news3.as_view(), name='news3'),
    path('news4/', views.news4.as_view(), name='news4'),
    path('news5/', views.news5.as_view(), name='news5'),
    path('news6/', views.news6.as_view(), name='news6'),
    path('news7/', views.news7.as_view(), name='news7'),
]