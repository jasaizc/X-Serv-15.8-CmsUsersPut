from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^login$',""),
  #  url(r'^logout',""),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^usuarios$', "cms_users_put.views.info"),
    url(r'^usuarios/(.*)$', "cms_users_put.views.valores"),
    url(r'^(.*)$', "cms_users_put.views.NotFound"),
)
