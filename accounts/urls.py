from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('account/signup', views.signup, name = 'signup'),
    path('account/signin', views.signin, name = 'signin'),
    path('account/writer', views.writer, name = 'writer'),
    path('account/writer', views.writer, name = 'writer'),
]