from django.urls import path
from consulting import views

app_name = 'consulting'
urlpatterns = [
    path('', views.AiConsultingView.as_view(), name='index'),
]