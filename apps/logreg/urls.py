from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name = "landing"),
	url(r'^register$', views.register, name = "register"),
	url(r'^login$', views.login, name = "login"),
	url(r'^logout$', views.logout, name = "logout"),
	url(r'^success$', views.success, name = "dashboard"),
	url(r'^user/(?P<user_id>\d+)$', views.person,name = "person")
	
]