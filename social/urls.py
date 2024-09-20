from django.urls import path

from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name='posts'),
    path('new/',views.CreatePostView.as_view(),name='create-post'),

    path('<int:pk>/update/',views.UpdatePostView.as_view(),name='update-post'),
    path('<int:pk>/delete/',views.DeletePostView.as_view(),name='delete-post'),
    path('my-posts/',views.get_user_posts,name='my-posts')



]
