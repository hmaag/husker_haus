from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, FormView
from django import forms
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from .models import Post, Comment
from .forms import CreateForm, CommentForm

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

class PostDetailForm(CommentForm):
    content = CommentForm

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(post=self.get_object())
        context['comments'] = comments
        context['form'] = PostDetailForm()
        return context

class PostCommentForm(SingleObjectMixin, FormView):
    template_name = 'aggregator/post_detail.html'
    form_class = PostDetailForm
    model = Post

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        content = form.cleaned_data.get('content')
        comment = Comment(post=self.get_object(), user=self.request.user, content=content)
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.pk})

class PostDetail(View):
    def get(self, request, *args, **kwargs):
        view = PostDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentForm.as_view()
        return view(request, *args, **kwargs)

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
