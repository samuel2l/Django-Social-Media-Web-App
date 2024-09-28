from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from .models import *

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

def post_details(request,pk):
    post = get_object_or_404(Post, id=pk)
    comments=Comment.objects.filter(post=pk).order_by('-date_created')

    return render(request,'post_details.html',{'post':post,'comments':comments})


def get_user_posts(request):
    posts = Post.objects.filter(author=request.user)
    if posts:
        return render(request,'posts.html',{'posts':posts})
    else:
        return  HttpResponse("You have no posts yet")

class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'create_comment.html'
    
    def form_valid(self, form):
        #use self.kwarges.get to access parameters passed

        post_id = self.kwargs.get('pk')  
        post = Post.objects.get(id=post_id)  

        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect back to the specific post after commenting
        return reverse('post-details', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs.get('pk')
        # Add the post to the context so we can view post while commenting
        context['post'] = Post.objects.get(id=post_id)  
        return context
    

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-date_created')
        followers=profile.followers.all()

        
        if request.user in followers:
            is_follower=True
        else:
            is_follower=False


        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'followers':len(followers),
            'is_follower':is_follower
        }

        return render(request, 'profile.html', context)

class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['name', 'bio','location', 'dp']
    template_name = 'edit_profile.html'
    success_url='profile/<int:pk>'

    def get_success_url(self):
            pk = self.kwargs['pk']
            return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
    
class Follow(LoginRequiredMixin,View):
    def post(self,request,pk,*args,**kwargs):
        profile=Profile.objects.get(pk=pk)
        
        profile.followers.add(request.user)
        return redirect('profile', pk=profile.pk)
    
class Unfollow(LoginRequiredMixin,View):
    def post(self,request,pk,*args,**kwargs):
        profile=Profile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)
    
class Like(LoginRequiredMixin,View):
    def post(self,request,pk,*args,**kwargs):
        post=Post.objects.get(pk=pk)
        print('requester',request.user)
        print('likes',post.likes)
        likes=post.likes.all()

        
        if request.user in likes:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        next=request.POST.get('next','/')
        return HttpResponseRedirect(next)
