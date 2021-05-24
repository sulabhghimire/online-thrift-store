from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import AdvertiseSell, Category, AdvertiseBuy
from django.views.generic import DetailView, ListView, DeleteView, UpdateView
from django.views.generic.edit import CreateView

def SearchTitle(request):
    if request.method == "POST":
        searched = request.POST['searched']
        title = AdvertiseSell.objects.filter(title__contains = searched)
        return render(request, 'blog/search_advertisement.html', {'searched': searched, 'posts': title} )
    else:
        return render(request, 'blog/search_advertisement.html')


def home(request):
    context = {
        'categories' : Category.objects.all(),
        'posts' : AdvertiseSell.objects.all().order_by('-id')[:16],
    }
    return render(request, 'blog/home.html', context)

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = AdvertiseSell.objects.filter(title__icontains=q)
        return render(request, 'blog/base.html', {'posts':posts})

class SellAdvertiseDetailView(DetailView):
    model = AdvertiseSell
    context_object_name = 'posts'
    template_name = 'blog/sell_advertisement_detail.html'

class AskAdvertiseDetailView(DetailView):
    model = AdvertiseBuy
    context_object_name = 'posts'
    template_name = 'blog/ask_advertisement_detail.html'

class SellingList(ListView):
    model = AdvertiseSell
    template_name = 'blog/selling_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class BuyingList(ListView):
    model = AdvertiseBuy
    template_name = 'blog/buying_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostItem(LoginRequiredMixin, CreateView):
    model = AdvertiseSell
    template_name = 'blog/list_form.html'
    fields = ['title', 'description', 'category', 'product_image', 'price', 'negotiable']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostItemUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AdvertiseSell
    template_name = 'blog/list_form.html'
    fields = ['title', 'description', 'category', 'product_image', 'price', 'negotiable']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostItemDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AdvertiseSell
    success_url = '/onsale_list/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SellItem(LoginRequiredMixin, CreateView):
    model = AdvertiseBuy
    template_name = 'blog/sell_form.html'
    fields = ['title', 'description', 'price', 'negotiable']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SellItemUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AdvertiseBuy
    template_name = 'blog/sell_form.html'
    fields = ['title', 'description', 'price', 'negotiable']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class SellItemDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AdvertiseBuy
    success_url = '/onask_list/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class YourSelling(LoginRequiredMixin, ListView):
    model = AdvertiseSell
    template_name = 'blog/my_selling.html'
    context_object_name = 'posts'

class YourAsking(LoginRequiredMixin, ListView):
    model = AdvertiseBuy
    template_name = 'blog/my_asking.html'
    context_object_name = 'posts'

def CategoriesPage(request, pk):
    context = {
        'categories' : Category.objects.get(id = pk),
        'posts' : AdvertiseSell.objects.all().order_by('-id')[:16],
    }
    return render(request, 'blog/categories.html', context)
