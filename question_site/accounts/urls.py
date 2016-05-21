from django.conf.urls import url
from .views import login_page, register, logout_page
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login_page'),
    url(r'^logout/$', logout_page, name='logout_page'),
    url(r'^register/$', register, name='register'),
]