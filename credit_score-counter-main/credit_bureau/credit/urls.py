from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_view, name='question_view'),  
    path('results/', views.result_view, name='result_view'),
]
