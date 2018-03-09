from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about', views.about, name='about'),
	path('ourteam', views.ourteam, name='ourteam'),
	path('ourmission', views.ourmission, name='ourmission'),
	path('ourpartners', views.ourpartners, name='ourpartners'),
	path('engage', views.engage, name='engage'),
	path('signup', views.signup, name='signup'),
	path('register', views.register, name='register'),
	path('register_user', views.register_user),
	path('login', views.login),
	path('yourcommunity', views.yourcommunity, name='yourcommunity'),
	path('getactive', views.getactive, name='getactive'),
	path('tulsa', views.tulsa, name='tulsa'),
	path('okc', views.okc, name='okc'),
	path('create_event', views.create_event, name='createevent'),
	
] + static(settings.STATIC_URL,
	document_root=settings.STATIC_ROOT)
