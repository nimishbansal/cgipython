from django.urls import path, include, re_path

from main_app import views

urlpatterns = [
    re_path(r'api/', include('main_app.api.urls')),
    re_path(r'^$', views.home),
]