from django.urls import path
from business import views

app_name = 'business'
urlpatterns = [
    # Example: /business/
    path('', views.BusinessView.as_view(), name='index'),
]
