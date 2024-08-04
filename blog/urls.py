from django.urls import path
from . import views
urlpatterns=[
    path('',views.starting_page,name='starting_page'),
    path('posts',views.posts,name='posts'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('submit',views.submit,name='submit'),
    path('posts/<slug:slug>',views.post_details,name='post_details'),
    path('<slug>',views.invalid)
    ]