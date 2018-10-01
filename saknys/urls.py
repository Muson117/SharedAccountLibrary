"""saknys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views


# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('accounts/', include('accounts.urls')),
    #path('admin/', admin.site.urls),
    path('accounts/', admin.site.urls),
    #path('login/', auth_views.login, name='login'),
    #path('logout/', auth_views.logout, {'next_page':'/'},name='logout'),
    #path('', RedirectView.as_view(url='/accounts/', permanent=True)),
    #path('', RedirectView.as_view(url='admin/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
