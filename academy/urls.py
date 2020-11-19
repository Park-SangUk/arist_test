from django.urls import path
from academy import views

app_name = 'academy'
urlpatterns = [

    path('', views.AcademyClassView.as_view(), name='index'),

    path('introduce/', views.IntroduceView.as_view(), name='introduce'),

    path('mathClass/', views.MathClassView.as_view(), name='math'),

    path('introduce/brginner/', views.BeginnerView.as_view(), name='beginner'),

    path('introduce/middle/', views.MiddleView.as_view(), name='middle'),

    path('introduce/machineLearning/', views.MachineLearningView.as_view(),
         name='machineLearning'),

    path('introduce/computerVision/', views.ComputerVisionView.as_view(),
         name='computerVision'),

     path('introduce/nlp/', views.NlpView.as_view(), name='nlp'),
]

#  # Example: /academy/
#     path('', views.LevelLV.as_view(), name='index'),

#     # Example: /academy/level/, same as /academy/
#     path('level/', views.LevelLV.as_view(), name='level_list'),

#     # Example: /academy/level/99/
#     path('level/<int:pk>/', views.LevelDV.as_view(), name='level_detail'),

#     # Example: /academy/contents/99/
#     path('contents/<int:pk>/', views.ContentsDV.as_view(), name='contents_detail'),
