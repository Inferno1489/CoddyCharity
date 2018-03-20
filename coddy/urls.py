from django.conf.urls import url
from coddy import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.main_site, name="main"),
    url(r'^en/$', views.main_site_en, name="main_en"),
    url(r'^donate/$', views.donate, name="donate"),
    url(r'^donate/en$', views.donate_en, name="donate_en"),
    url(r'^volunteer/$', views.volunteer, name="volunteer"),
    url(r'^volunteer/en$', views.volunteer_en, name="volunteer_en"),
]