from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.post_list, name='post_list'),
    path('', views.index, name='index'),
    path('turtle/', views.turtle, name='turtle'),
    path('accounts/register/', views.register, name='register'),
    path('work/', views.work, name='work'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]
