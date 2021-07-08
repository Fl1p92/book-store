from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('book/create/', views.CreateBookView.as_view(), name='create'),
    path('book/edit/<int:book_id>/', views.EditBookView.as_view(), name='edit'),
]
