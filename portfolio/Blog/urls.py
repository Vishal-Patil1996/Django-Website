from. import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('services.html', views.services),
    path('contact.html', views.contacts, name='contact'),
    path('blog.html', views.blog),
    path('blog-single.html', views.single),

]