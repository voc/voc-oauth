from django.contrib.auth import views as auth_views
try:
    from django.urls import include, url
except ImportError:
    from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^oauth/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^oauth/accounts/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^oauth/accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^oauth/', include('oidc_provider.urls', namespace='oidc_provider')),
    url(r'^oauth/admin/', admin.site.urls),
]
