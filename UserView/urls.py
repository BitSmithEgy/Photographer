from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('packages/', views.packages, name='packages'),
    path('video-packages/', views.videography, name='videography'),
    path('cinema-packages/', views.cinematography, name='cinematography')
]
