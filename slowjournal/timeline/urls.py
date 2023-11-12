from django.urls import path

from . import views

urlpatterns = [
    path('', views.timeline, name="index"),
    path('timeline/', views.timeline, name="timeline"),
    path('user/', views.user, name='user')
]
