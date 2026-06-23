from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'core/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'core/post_form.html'
    fields = ['title', 'content', 'published_date', 'author']

    def get_success_url(self):
        return f'/post/{self.object.pk}/'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'core/post_form.html'
    fields = ['title', 'content', 'published_date', 'author']

    def get_success_url(self):
        return f'/post/{self.object.pk}/'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'core/post_confirm_delete.html'
    success_url = reverse_lazy('core:post_list')