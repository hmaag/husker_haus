from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post
from .forms import CreateForm

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'aggregator/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'aggregator/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 30

def UserProfileView(request, **kwargs):
    model = User
    username = kwargs.get('username')
    user = User.objects.filter(username=username).first()
    created = user.date_joined
    context = {
        'username': username,
        'created': created,
    }
    return render(request, 'aggregator/user_profile.html', context)

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'aggregator/about.html', {'title': 'About'})
