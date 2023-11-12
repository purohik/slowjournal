from django.urls import path

from . import views

urlpatterns = [
    path('', views.timeline, name="index"),
    path('user/', views.user, name='user'),
    path('timeline/', views.timeline, name="timeline"),
    path('timeline/<str:username>', views.user_timeline, name="user_timeline")
]
