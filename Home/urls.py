from django.urls import path
from django.conf.urls.static import static

from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('consultancies',views.consultancies,name='consultancies'),
    path('events',views.events,name='events'),
    path('offers',views.offers,name='offers'),
    path('blog',views.blog,name='blog'),
    path('test-prep',views.test,name='test'),
    path('contact',views.contact,name='contact'),
]
