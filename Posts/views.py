from django.shortcuts import render, HttpResponseRedirect
from django.views import generic

from Posts.models import Post
from .forms import PostForm

def newstory(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = PostForm()
    return render(request, 'Posts/newstory.html', {'form': form})

def stories(request):
    stories = Post.objects.all()
    return render(request, 'Posts/stories.html', {'stories': stories })

def view_post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'Posts/view_post.html', {'post': post})

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/confirmed")
    else:
        form = PostForm()
    return render(request, "posts/newpost.html", {'form': form})

def edit_post(request, slug):
    if request.method == 'POST':
        post = Post.objects.get(slug=slug)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        post = Post.objects.get(slug=slug)
        form = PostForm(instance=post)
    return render(request, "posts/edit_post.html", {'form': form, 'post': post})

def delete_story(request, id):
    if request.method == 'POST':
        Post.objects.get(id=id).delete()
        return HttpResponseRedirect("/")
    else:

        return render(request, 'Posts/stories')


class Confirmed(generic.DetailView):
    """
    This view will display confirmation on a successful post
    """
    template_name = 'confirmed.html'

    def get(self, request):
        return render(request, 'confirmed.html')