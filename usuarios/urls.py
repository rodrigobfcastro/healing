from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.sair, name="sair"),
    path('', views.login_view, name="login"),  
]
