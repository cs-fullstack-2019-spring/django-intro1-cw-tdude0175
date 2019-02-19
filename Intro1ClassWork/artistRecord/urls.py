from django.urls import path
from . import views

urlpatterns = \
    [
        path('',views.badRoute, name ="default"),
        path('music/',views.index, name = 'index'),
        path('music/artistOne/',views.artOne, name = 'basic'),
        path('music/artistTwo/', views.artTwo, name = 'secondary'),
        path('music/artistThree/',views.artThree,name = 'final')
    ]
