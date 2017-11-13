from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
#
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/', login, {'template_name': 'templates/login.html'}),
	url(r'^profiles/',views.profiles, name = 'profiles'),
  	url(r'^signup/', views.signup, name = 'signup'),
  	url(r'^careers/',views.careers, name = 'careers'),
    
 
    




    #url(r'^login/$', index,{{'template_name': 'templates/index.html' }})
]