from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.listaCensos, name='census_create'),
    path('<int:voting_id>/', views.listaVotantes, name='census_detail'),
]
