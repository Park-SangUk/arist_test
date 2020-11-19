from django.urls import path
from lecture import views

app_name = 'lecture'
urlpatterns = [
    # Example: /lecture/
    path('', views.LectureView.as_view(), name='index'),
]
