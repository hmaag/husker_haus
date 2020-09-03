from django.urls import path
from .views import PostListView, PostDetail, PostDetailView, PostCreateView, PostDeleteView, UserProfileView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='site-home'),
    path('user/<str:username>', views.UserProfileView, name='user-profile'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='site-about')
]