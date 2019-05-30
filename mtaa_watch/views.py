from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from .models import Post, Neighborhood, Business, Contact


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'mtaa_watch/home.html', context)

# List Views for Post, Business and Neighborhood

class PostListView(ListView):
    model = Post
    template_name = 'mtaa_watch/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class NeighborhoodListView(ListView):
    model = Neighborhood
    template_name = 'mtaa_watch/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'neighborhoods'
    ordering = ['business_location']
    
class BusinessListView(ListView):
    model = Business
    template_name = 'mtaa_watch/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'businesses'
    ordering = ['business_name']

class ContactListView(ListView):
    model = Contact
    template_name = 'mtaa_watch/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'contacts'
    ordering = ['contact_name']

# Detail Views for Post, Business and Neighborhood
class PostDetailView(DetailView):
    model = Post

class NeighborhoodDetailView(DetailView):
    model = Neighborhood

class BusinessDetailView(DetailView):
    model = Business

class ContactDetailView(DetailView):
    model = Contact

# Create Views for Post, Business and Neighborhood
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'mtaa_watch/about.html', {'title': 'About'})
