from django.urls import path
from . import views

urlpatterns = \
    [
        path('',views.index, name = 'index'),
        path('artistOne/',views.artOne, name = 'basic'),
        path('artistTwo/', views.artTwo, name = 'secondary'),
        path('artistThree/',views.artThree,name = 'final')
    ]