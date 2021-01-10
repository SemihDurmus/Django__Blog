from django.shortcuts import render, redirect, get_object_or_404
#from django.http import HttpResponse
from .models import Post, Like
from .forms import PostForm, CommentForm


def post_list(request):
    qs = Post.objects.filter(status="p")
    context = {
        "object_list": qs
    }
    return render(request, "blog/post_list.html", context)


def post_create(request):
    #form = PostForm(request.POST or None, request.FILES or None)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # means save the post but not add to db yet
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:list")
    context = {
        'form': form
    }
    return render(request, "blog/post_create.html", context)


def post_detail(request, slug):
    form = CommentForm
    obj = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = obj
            comment.save()
            return redirect("blog:detail", slug=slug)
    context = {
        'object': obj,
        "form": form
    }
    return render(request, "blog/post_detail.html", context)


def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.user.id != obj.author.id:
        return redirect("blog:list")
        # return HttpResponse("You are not authorized")
    form = PostForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("blog:list")
    context = {
        'object': obj,
        'form': form
    }
    return render(request, "blog/post_update.html", context)


def post_delete(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    if request.user.id != obj.author.id:
        return redirect("blog:list")
        # return HttpResponse("You are not authorized")
    if request.method == "POST":
        obj.delete()
        return redirect("blog:list")
    context = {
        "object": obj
    }
    return render(request, "blog/post_delete.html", context)


def like(request, slug):

    if request.method == "POST":
        obj = get_object_or_404(Post, slug=slug)
        like_qs = Like.objects.filter(user=request.user, post=obj)

        if like_qs:
            like_qs[0].delete()
        else:
            Like.objects.create(user=request.user, post=obj)
        return redirect('blog:detail', slug=slug)
