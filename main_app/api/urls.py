from django.urls import path, include, re_path

from main_app.api import views

urlpatterns = [
    re_path(r'games/$', views.GamesListAPIView.as_view()),
    re_path(r'games/(?P<pk>[0-9]+)/', views.GameDetailAPIView.as_view()),
]