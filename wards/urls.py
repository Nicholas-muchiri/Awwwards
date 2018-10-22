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
    url(r'^post/(?P<project_id>[0-9]+)/review_design/$', views.add_design, name='add_design'),
    url(r'^post/(?P<project_id>[0-9]+)/review_usability/$', views.add_usability, name='review_usability'),
    url(r'^post/(?P<project_id>[0-9]+)/review_content/$', views.add_content, name='review_content'),


    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)