from django.contrib import admin
from django.urls import path, include

from arist.views import HomeView

from django.conf.urls.static import static
from django.conf import settings

import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('business/', include('business.urls')),
    path('academy/', include('academy.urls')),
    path('lecture/', include('lecture.urls')),
    path('consulting/', include('consulting.urls')),
    path('blog/', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
