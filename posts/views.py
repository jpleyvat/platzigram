"""Post Views."""

#Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import ListView

#Form
from posts.forms import PostForm


#Models
from django.contrib.auth.models import User
from posts.models import Post

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    context_object_name = 'posts'


@login_required
def create_post(request):
    """Create new post view"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')

    else:
        form = PostForm()

    return render(
        request = request,
        template_name='posts/new.html',
        context = {
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )

class PostDetailView(LoginRequiredMixin, DetailView):
    """Post detail view"""

    template_name = 'posts/detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    queryset = Post.objects.all()



