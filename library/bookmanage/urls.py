from django.urls import path

from . import views

app_name = 'bookmanage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<str:name>/getrentbook/', views.GetRentBook, name='getrentbook'),
    path('searchbook/', views.SearchBook, name='searchbook'),
    path('operatebook/', views.OperateBook, name='operatebook'),
]