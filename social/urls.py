from django.urls import path

from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='posts'),
    path('new/',views.CreatePostView.as_view(),name='create-post'),

    path('<int:pk>/update/',views.UpdatePostView.as_view(),name='update-post'),
    path('<int:pk>/delete/',views.DeletePostView.as_view(),name='delete-post'),
    path('<int:pk>/',views.post_details,name='post-details'),
    path('<int:pk>/comment/',views.CreateCommentView.as_view(),name='comment'),
    path('my-posts/',views.get_user_posts,name='my-posts'),
    path('profile/<int:pk>/',views.ProfileView.as_view(),name='profile'),
    path('edit-profile/<int:pk>/',views.EditProfileView.as_view(),name='edit-profile'),
    path('profile/<int:pk>/follow/',views.Follow.as_view(),name='follow'),
    path('profile/<int:pk>/unfollow/',views.Unfollow.as_view(),name='unfollow'),
   
    path('post/<int:pk>/like/',views.Like.as_view(),name='like'),

    path('search/',views.SearchUser.as_view(),name='search_results'),

    



]
