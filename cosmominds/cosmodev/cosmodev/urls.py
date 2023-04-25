"""cosmodev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

from .views import(IndexViewPage)
 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard',IndexViewPage.as_view(),name='dashboard'),
    
    path('tweet/', include(('myapp.urls','tweet'),namespace='tweet')),
    path('api/tweet',include(('myapp.api.urls','tweet-api'), namespace='tweet-api')),

    
]
if settings.DEBUG:
    urlpatterns+= (static(settings.STATIC_URL,document_root = settings.STATIC_ROOT))