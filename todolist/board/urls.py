from django.urls import path , include
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('completed/<int:id>/', views.completed, name='completed'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
]