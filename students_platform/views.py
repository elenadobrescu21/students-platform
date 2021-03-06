from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Forum
from django.shortcuts import redirect
from .forms import PostForm

# Create your views here.

def forum_list(request):
    forums= Forum.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'students_platform/forum_list.html', {'forums': forums})


def post_list(request, forum_name):
    posts = Post.objects.filter(forum__title__exact = forum_name)
    return render(request, 'students_platform/post_list.html', {'posts': posts})

def post_details(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return 	render(request, 'students_platform/post_details.html', {'post':post})

def forum_details(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    posts = Post.objects.filter(forum__title__exact=forum.title)
    return 	render(request, 'students_platform/forum_details.html', {'forum':forum,'posts':posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('students_platform.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'students_platform/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('students_platform.views.post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'students_platform/post_edit.html', {'form': form})
