from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[
    path('',views.login,name='login'),
    path('tryLogin/',views.tryLogin,name='tryLogin'),
    path('home/',views.home,name='home'),
    path('formularioCarla/',views.formularioCarla,name='formularioCarla'),
    path('formularioDiego/',views.formularioDiego,name='formularioDiego'),
    path('registro/', views.registro, name='registro'),
    path('registro/tryRegistrar/', views.tryRegistrar, name='tryRegistrar'),

]