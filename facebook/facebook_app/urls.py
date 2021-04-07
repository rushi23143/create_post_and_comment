from django.contrib import admin
from django.urls import path
from . import views
#from .views import friend_list, friend_request

urlpatterns = [
    path('', views.navigate, name='navigate'),
    path('base/', views.base, name='base'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('create_post/', views.create_post, name='create_post'),
    path('readmore/<int:id>', views.readmore, name='readmore'),
    #path('friend_list/', friend_list.as_view(), name='friend_list'),
    #path('friend_request/', friend_request.as_view(), name='friend_request'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin/admin_panel', views.admin_panel, name='admin_panel'),
    path('admin/admin_blog', views.admin_blog, name='admin_blog'),
    path('admin/admin_coment', views.admin_coment, name='admin_coment'),
    path('admin/admin_flist', views.admin_flist, name='admin_flist'),
    path('admin/admin_frequest', views.admin_frequest, name='admin_frequest'),
    path('admin/users', views.users, name='users'),
    #path('comment/', views.comment, name='comment')
]