from django.urls import path
from .views import feed_view
from .views import signup_view, login_view, logout_view, upload_post_view, upload_product_view, store_view, post_likes, get_liked_users, profile_view

urlpatterns = [
    path('', feed_view, name='home'),
    path('home/', feed_view , name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('upload/', upload_post_view, name='upload'),
    path('upload_product/', upload_product_view, name='upload_product'),
    path('store/', store_view, name='store'),
    path('post_like/<int:pk>', post_likes, name='post_like'),
    path('liked_users/<int:pk>/', get_liked_users, name='liked_users'),
    path('profile/<str:username>/', profile_view, name='profile')
]
