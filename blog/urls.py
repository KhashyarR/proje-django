from django.urls import path
from .views import PostView, PostDetail, PostCreate, PostUpdate, PostDelete, UserView, UserDetail, UserCreate, UserUpdate, UserDelete

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('store/<int:pk>/', PostDetail.as_view(),name='post_detail'),
    path('store/new/', PostCreate.as_view(), name='post_new'),
    path('store/<int:pk>/edit/',PostUpdate.as_view(), name='post_edit'),
    path('store/<int:pk>/delete/',PostDelete.as_view(), name='post_delete'),
    path('users/', UserView.as_view(), name='users'),
    path('users/user/<int:pk>/', UserDetail.as_view(),name='user_detail'),
    path('users/user/new/', UserCreate.as_view(), name='user_new'),
    path('users/user/<int:pk>/edit/',UserUpdate.as_view(), name='user_edit'),
    path('users/user/<int:pk>/delete/',UserDelete.as_view(), name='user_delete'),
]
