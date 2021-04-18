from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView, 
                    UserUpdateView, 
                    ProfileCreateView, 
                    CommentCreateView,
                    UserCreateView
                    )
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/add_posts/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/', views.profile_view, name='profile_view'),
    path('users/makeprofile/', UserCreateView.as_view(), name='create_profile'),
    path('posts/<int:pk>/add_comment/', CommentCreateView.as_view(), name='create_comment'),
    path('posts/<int:pk>/like/', views.LikeView, name='blog_like')
]