from django.urls import path

from moneytrack_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings')
]