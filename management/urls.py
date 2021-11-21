from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/', views.view, name='view'),
    path('view-user/<str:pk>/', views.user_view, name='user-view'),
    path('create/', views.create_user, name='create'),
    path('chart/<str:pk>/', views.chart, name='chart')
]
