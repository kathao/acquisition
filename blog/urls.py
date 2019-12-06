from django.urls import path
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView,
    PostAddNew
	)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/add/new/', PostAddNew.as_view(), name='post-add'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('acquisition/', views.upload_book, name='blog-acquisition'),
    path('acquisition/list', views.book_list, name='blog-book_list'),
    path('books/upload', views.upload_book, name='blog-upload_book'),
    path('books/<int:pk>/', views.delete_book, name='blog-delete_book'),
    path('add/rsvp/', views.upload_rsvp, name='blog-upload_rsvp'),
    path('rsvp/list', views.rsvp_list, name='blog-rsvp_list'),
    path('rsvps/<int:pk>/', views.delete_rsvp, name='blog-delete_rsvp'),
    path('rsvps/template/', views.rsvp_template, name='blog-rsvp_template'),
    # path('', views.index),

]