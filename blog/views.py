from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from . import forms

from . import models


def home_page(request):
    return render(request, "home.html")


def posts_list_view(request):
    posts = models.Post.objects.filter(status="pub").order_by("-datetime_created")

    return render(request, "blog/posts_list.html", {"posts": posts})


def post_detail_view(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def post_create_view(request):
    if request.method == "POST":
        form = forms.NewPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            # form = forms.NewPostForm()
            # return redirect(reverse("posts_list"))
            # return redirect("posts_list")
            return redirect(post.get_absolute_url())

    else:
        form = forms.NewPostForm()
    return render(request, "blog/post_create.html", {"form": form})


def post_update_view(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    form = forms.NewPostForm(request.POST or None, instance=post)

    if form.is_valid():
        post = form.save()
        return redirect(post.get_absolute_url())

    return render(request, "blog/post_create.html", {"form": form})


def post_delete_view(request, pk):
    post = get_object_or_404(models.Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("posts_list")

    return render(request, "blog/post_delete.html", {"post": post})
