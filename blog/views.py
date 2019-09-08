from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogAbout(ListView):
    model = Post
    template_name = 'about.html'

class BlogApp(ListView):
    model = Post
    template_name = 'app.html'

class BlogPrice(ListView):
    model = Post
    template_name = 'price.html'

class BlogContacts(ListView):
    model = Post
    template_name = 'contacts.html'

class BlogDelivery(ListView):
    model = Post
    template_name = 'delivery.html'

# Create your views here.
