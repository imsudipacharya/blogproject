"""
URL configuration for acharya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sudip.urls')),
    path('about/', include('sudip.urls')),
    path('works/', include('sudip.urls')),
    path('work-details/', include('sudip.urls')),
    path('service/', include('sudip.urls')),
    path('contact/', include('sudip.urls')),
    path('credentials/', include('sudip.urls')),
    path('category/', include('sudip.urls')),
    path('blog/', include('sudip.urls')),
    path('blog-details/', include('sudip.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
