"""Defines Patterns for BOS urls"""
from django.urls import path
from . import views

app_name = 'bos'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    #Page that shows BOS's
    path('bos/', views.bos, name='bos'),
    # Detail page for a single BOS
    path('showbos/<int:bos_id>/',views.showbos, name='show bos'),
    # BOS entry
    path('new_bos/', views.new_bos, name='new_bos'),

]