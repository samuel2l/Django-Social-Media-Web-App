from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from .models import Post

# Create your views here.
class HomeView(ListView):
    model=Post
    template_name='posts.html'
    context_object_name='posts'
    ordering=['-date_created']


class CreatePostView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['content']
    template_name='create_post.html'
    
    success_url='/posts'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['content']

    template_name='create_post.html'
    success_url='/posts'

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
    
class DeletePostView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name='confirm_delete.html'
    success_url='/posts'

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

def get_user_posts(request):
    user_posts = Post.objects.filter(author=request.user)
    return render(request,'posts.html',{'posts':user_posts})

