from django.urls import path

from . import views


urlpatterns = [
    path('logs/', views.LogView.as_view(), name='index'),
]