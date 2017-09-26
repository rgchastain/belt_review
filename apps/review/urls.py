from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.home, name = "home"),
	url(r'^add$', views.add, name="add"),
	url(r'^create$', views.create, name = "create"),
	url(r'^show/(?P<book_id>\d+)$', views.show, name = "show"),
]