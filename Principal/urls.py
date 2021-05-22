"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf.urls import url, include
from django.contrib import admin
#from django.contrib.auth import login
from django.contrib.auth.views import LoginView

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.config.urls.static import static





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'registro', include('usuario.urls')),
    path ('', include('inicio.urls')),
    
    url(r'inicio',LoginView.as_view(template_name='Inicio_Sesion.html'),name='login'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="olvidoContrase.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html") ,name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),




    #url(r'^$',login, {'template_name':'Inicio_Sesion.html'},name='login'),


]+static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
