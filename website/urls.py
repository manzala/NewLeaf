from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
#
urlpatterns = [
	
	url(r'^login/', login, {'template_name': 'templates/login.html'}),
  	url(r'^signup/', views.signup, name = 'signup'),
    url(r'^$', views.login, name=''),
 
    




    #url(r'^login/$', index,{{'template_name': 'templates/index.html' }})
]