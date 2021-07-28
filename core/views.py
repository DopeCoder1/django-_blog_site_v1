from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import *
from .utils import *


# Create your views here.
# def home_page(request):
#     post = Blog.objects.all()
#     cats = Category.objects.all()
#     context = {
#         'post': post,
#         'cats': cats,
#     }
#     return render(request, 'core/index.html', context)
#
#
# def post_details(request, post_slug):
#     post = get_object_or_404(Blog, slug=post_slug)
#     context = {
#         'post': post,
#     }
#     return render(request, 'core/post_details.html', context)
#
#
# def show_category(request, cat_slug):
#     post = Blog.objects.filter(cat__slug=cat_slug)
#     cats = Category.objects.all()
#     context = {
#         'cats': cats,
#         'post': post,
#     }
#     return render(request, 'core/index.html', context)
#
#
# @login_required
# def addpage(request):
#     if request.method == 'POST':
#         form = BlogForms(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('index')
#     else:
#         form = BlogForms()
#     return render(request, 'core/addpage.html', {'form': form})


class HomeView(DataMixin, ListView):
    model = Blog
    template_name = 'core/index.html'
    context_object_name = "post"
    post = Blog.objects.all()

    # cats = Category.objects.all()
    # extra_context = {"cats": cats}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home page"
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class CategoryView(DataMixin, ListView):
    model = Blog
    template_name = 'core/index.html'
    context_object_name = 'post'

    # cats = Category.objects.all()
    # extra_context = {'cats': cats}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


class PostView(DataMixin, DetailView):
    model = Blog
    template_name = 'core/post_details.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class AddPageView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = BlogForms
    template_name = 'core/addpage.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('index')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))
