from django.conf.urls import include, url
from django.contrib import admin
from homepage.views import search

app_name = 'main'

urlpatterns = [
    url(r'^questions/', include('stacked.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^search/$', search, name='search'),
    url(r'^$', include('homepage.urls')),
]
