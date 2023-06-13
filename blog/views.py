from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.shortcuts import redirect
from django.views.generic.list import ListView

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# Servicios 


class ServiciosListView(ListView):
    model = servicios
    template_name = 'blog/servicios_list.html'
    context_object_name = 'servicio'

def servicios_detail(request, pk):
    servicio = get_object_or_404(servicios, pk=pk)
    return render(request, 'blog/servicios_detail.html', {'servicio': servicio})

def servicios_new(request):
    if request.method == "POST":
        form = serviciosForm(request.POST)
        if form.is_valid():
            servicios = form.save(commit=False)
            servicios.save()
            return redirect('servicios_detail', pk=servicios.pk)
    else:
        form = serviciosForm()
    return render(request, 'blog/servicios_edit.html', {'form': form})

def servicios_edit(request, pk):
    servicio = get_object_or_404(servicios , pk=pk)
    if request.method == "POST":
        form = serviciosForm(request.POST, instance=servicio)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.save()
            return redirect('servicios_detail', pk=servicio.pk)
    else:
        form = serviciosForm(instance=servicio)
    return render(request, 'blog/servicios_edit.html', {'form': form})
