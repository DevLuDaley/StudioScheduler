"""studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static, serve
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers

from rest_framework.routers import DefaultRouter

import scheduler.views
import scheduler.api_views
# from projectstudio.scheduler import views

app_name = 'scheduler'

router = routers.DefaultRouter()
# router.register(r'artists', scheduler.views.ArtistViewSet, 'artist')
router.register(r'artists', scheduler.views.ArtistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/artists/', scheduler.api_views.ArtistList.as_view()),
    path('api/v1/sessions/', scheduler.api_views.SessionList.as_view()),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', scheduler.views.home, name='home'),
    path('artists/', scheduler.views.artists, name='artists'),
    path('studios/', scheduler.views.studios, name='studios'),
    path('engineers/', scheduler.views.engineers, name='engineers'),
    path('createsession/', scheduler.views.createsession, name='createsession'),
    path('sessions/', scheduler.views.sessions, name='sessions'),
    re_path(r'^(?P<path>.*)$', serve),
    re_path(r'^api/v1/artists/$', scheduler.views.artists_list),
    path('api/', include(router.urls)),
    #        {'document_root': settings.FRONTEND_ROOT}),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# url(r'^api-auth/', include('rest_framework.urls'))
