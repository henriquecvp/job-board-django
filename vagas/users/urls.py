from django.urls import path
from . import views

urlpatterns = [
    path('entrar', views.login_user, name='Login'),
    path('cadastrar', views.create_user, name='Signup'),
    path('sair', views.logout_user, name='Signout'),
]