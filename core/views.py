from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from django.urls import reverse, reverse_lazy
from .models import Post, Product
from .forms import ContactoForm, ProductSearchForm


class HomeView(TemplateView):
    template_name = 'core/home.html'


class AboutView(TemplateView):
    template_name = 'core/about.html'


class ContactoView(FormView):
    template_name = 'core/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('core:contacto')

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form, enviado=True))


def products(request):
    form = ProductSearchForm(request.GET)
    query = ''
    category = ''
    products_qs = Product.objects.filter(active=True)

    if form.is_valid():
        query = form.cleaned_data.get('q', '').strip()
        category = form.cleaned_data.get('category', '').strip()

        if query:
            products_qs = products_qs.filter(name__icontains=query)
        if category:
            products_qs = products_qs.filter(category__icontains=category)

    return render(request, 'core/products.html', {
        'form': form,
        'products': products_qs,
        'query': query,
        'category': category,
    })


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
        return reverse('core:post_detail', kwargs={'pk': self.object.pk})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'core/post_form.html'
    fields = ['title', 'content', 'published_date', 'author']

    def get_success_url(self):
        return reverse('core:post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'core/post_confirm_delete.html'
    success_url = reverse_lazy('core:post_list')