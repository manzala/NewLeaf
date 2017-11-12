from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
#
urlpatterns = [
	url(r'^login/', login, {'template_name': 'templates/login.html'}),
	url(r'^profiles/',views.profiles, name = 'profiles'),
  	url(r'^signup/', views.signup, name = 'signup'),
    url(r'^', views.index, name='index'),
 
    




    #url(r'^login/$', index,{{'template_name': 'templates/index.html' }})
]