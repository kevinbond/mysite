from django.conf.urls.defaults import *
 
from hello.views import hello

urlpatterns = patterns('',
('^hello/$', hello)
 
)