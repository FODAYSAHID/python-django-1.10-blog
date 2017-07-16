from django.conf.urls import url
from .import views

app_name = "blog"

urlpatterns = [
	
		url(r'^$', views.index, name = 'index'),
		url(r'^category/(?P<slug>\S+)/$', views.categoryContent, name = 'category-content'),
		url(r'^blog/post-content/(?P<slug>\S+)/$', views.postContent, name = 'post-content'),
		url(r'^contact/$', views.contactMe, name = 'contact-me'),
		url(r'^thanks-for-contacting-me/$', views.mailOnSuccess, name = 'thanks-for-contacting'),
		url(r'^about/$', views.aboutMe, name = 'about-me'),
		url(r'^blog-list/$', views.blogPost, name = 'blog-list'),
]
