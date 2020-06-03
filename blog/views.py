from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #
# this module is used so that users who are not logged in need
# sign then only they can create post
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  ) # these are class based view
from .models import Post
from django.shortcuts import redirect


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post  # app/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post  # app/<model>_<viewtype>.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # app/<model>_<viewtype>.html
    fields = ['title', 'content']
    # success_url = '/' the new post will return back to  the home page

    def form_valid(self, form):  # this function is created
        # so that author gets created with the current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  # app/<model>_<viewtype>.html
    fields = ['title', 'content']
    # success_url = '/' the new post will return back to  the home page

    def form_valid(self, form):  # this function is created
        # so that author gets created with the current logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        We are creating that function so that only author can update their post
        and no one else can temper their post

        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  # app/<model>_<viewtype>.html
    success_url = '/'

    def test_func(self):
        """
        We are creating that function so that only author can update their post
        and no one else can temper their post

        """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')

