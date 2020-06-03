from . import views
from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    )

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about')
]
"""
    We don't need to create template for new post url and post update because 
    they will be using the  post create template
"""
