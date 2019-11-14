from django.contrib.auth import views as auth_views
try:
    from django.urls import include, url
except ImportError:
    from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import oidc_provider.views as views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^', include('oidc_provider.urls', namespace='oidc_provider')),
    url(r'^oauth/token/?$', views.TokenView.as_view(), name='oidc_provider.token'),
    url(r'^admin/', admin.site.urls),
]
