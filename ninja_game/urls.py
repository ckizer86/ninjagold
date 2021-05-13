from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money', views.process_money),
    path('reset_activity', views.reset_activity),
    path('reset_gold', views.reset_gold),
    path('reset_all', views.reset_all),
]