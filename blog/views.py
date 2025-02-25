from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from . import forms
from . import models



class HomePage(generic.TemplateView):
    template_name = "home.html"


class PostListView(generic.ListView):
    # model = models.Post
    template_name = "blog/posts_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return models.Post.objects.filter(status="pub").order_by("-datetime_created")


class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(generic.CreateView):
    # model = models.Post
    # fields = ['title','text','author','status']
    form_class = forms.NewPostForm
    template_name = "blog/post_create.html"


class PostUpdateView(generic.UpdateView):
    model = models.Post
    form_class = forms.NewPostForm
    template_name = "blog/post_create.html"


class PostDeleteView(generic.DeleteView):
    model = models.Post
    template_name = "blog/post_delete.html"
    # success_url = reverse_lazy('posts_list')

    def get_success_url(self):
        return reverse("posts_list")


# Functional view
# ========
# def posts_list_view(request):
#     posts = models.Post.objects.filter(status="pub").order_by("-datetime_created")

#     return render(request, "blog/posts_list.html", {"posts": posts})
# ------------------------------------------
# def post_detail_view(request, pk):
#     post = get_object_or_404(models.Post, pk=pk)
#     return render(request, "blog/post_detail.html", {"post": post})
# ------------------------------------------
# def post_create_view(request):
#     if request.method == "POST":
#         form = forms.NewPostForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             # form = forms.NewPostForm()
#             # return redirect(reverse("posts_list"))
#             # return redirect("posts_list")
#             return redirect(post.get_absolute_url())

#     else:
#         form = forms.NewPostForm()
#     return render(request, "blog/post_create.html", {"form": form})
# ------------------------------------------
# def post_update_view(request, pk):
#     post = get_object_or_404(models.Post, pk=pk)
#     form = forms.NewPostForm(request.POST or None, instance=post)

#     if form.is_valid():
#         post = form.save()
#         return redirect(post.get_absolute_url())

#     return render(request, "blog/post_create.html", {"form": form})
# ------------------------------------------
# def post_delete_view(request, pk):
#     post = get_object_or_404(models.Post, pk=pk)

#     if request.method == "POST":
#         post.delete()
#         return redirect("posts_list")

#     return render(request, "blog/post_delete.html", {"post": post})
