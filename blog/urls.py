from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [
    # Example: /blog/
    path('', views.PostLV.as_view(), name='index'),
    # /blog/post/
    path('post/', views.PostLV.as_view(), name='post_list'),
    # /blog/post/detail/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
]