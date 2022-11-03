from django.urls import path

from . import views

urlpatterns = [
    path('', views.Sample, name='profile'),
    path('value', views.SamplePost, name='value')
]