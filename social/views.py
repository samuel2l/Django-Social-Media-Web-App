from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post

# Create your views here.
class HomeView(ListView):
    model=Post
    template_name='home.html'
    context_object_name='posts'#defines the name of the context you are sending to your template. by default it is called object
    ordering=['-date_created'] #field on which to order results. -date means date in descending order
