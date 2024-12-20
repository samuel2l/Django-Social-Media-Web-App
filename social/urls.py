from django.urls import path

from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='posts'),
    path('new/',views.CreatePostView.as_view(),name='create-post'),
    path('<int:pk>/update/',views.UpdatePostView.as_view(),name='update-post'),
    path('<int:pk>/delete/',views.DeletePostView.as_view(),name='delete-post'),
    path('<int:pk>/',views.post_details,name='post-details'),
    path('<int:pk>/comment/',views.CreateCommentView.as_view(),name='comment'),
    path('<int:pk>/comment/<int:comment_pk>/like-comment',views.LikeComment.as_view(),name='like-comment'),
    path('<int:pk>/comment/<int:comment_pk>/reply-comment',views.CreateCommentReplyView.as_view(),name='reply-comment'),

    path('my-posts/',views.get_user_posts,name='my-posts'),
    path('profile/<int:pk>/',views.ProfileView.as_view(),name='profile'),
    path('edit-profile/<int:pk>/',views.EditProfileView.as_view(),name='edit-profile'),
    path('profile/<int:pk>/follow/',views.Follow.as_view(),name='follow'),
    path('profile/<int:pk>/unfollow/',views.Unfollow.as_view(),name='unfollow'),   
    path('post/<int:pk>/like/',views.Like.as_view(),name='like'),
    path('search/',views.Search.as_view(),name='search_results'),
    path('profile/<int:pk>/followers/',views.Followers.as_view(),name='followers'),
 path('<int:notification_pk>/notification/post/<int:post_pk>', views.PostNotification.as_view(), name='post-notification'),
    path('<int:notification_pk>/notification/profile/<int:profile_pk>', views.FollowNotification.as_view(), name='follow-notification'),
    path('<int:notification_pk>/notification/delete', views.RemoveNotification.as_view(), name='delete-notification'),
    path('chats/',views.ListChats.as_view(),name='chat-list'),
    path('chats/create-chat',views.CreateChat.as_view(),name='create-chat'),
path('chats/<int:pk>',views.ChatView.as_view(),name='chat'),
path('chats/<int:pk>/create-message',views.CreateMessageView.as_view(),name='create-message')    

    ]
