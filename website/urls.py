from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
#
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^login/', views.loginReq, name = 'login'),
	url(r'^profiles/',views.profiles, name = 'profiles'),
  	url(r'^signup/', views.signupReq, name = 'signup'),
  	url(r'^careers/',views.careers, name = 'careers'),
    
 
    




    #url(r'^login/$', index,{{'template_name': 'templates/index.html' }})
]