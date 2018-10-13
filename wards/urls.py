from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$', views.awards, name='awards'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^upload/$', views.upload_project, name='upload_project'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^search/', views.search, name='search'),
    url(r'^edit/',views.edit_profile, name='edit_profile'),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)