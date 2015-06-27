

from django.shortcuts import render
from django.utils import timezone
from .models import Post,Forum

def forum_list(request):
    forums= Forum.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'students_platform/post_list.html', {'forums': forums})

def post_list(request, forum_name):
    posts = Post.objects.filter(forum__title__exact = forum_name().order_by('published_date')
    return render(request, 'blog/post_list.html', {
    	'posts': posts
    	})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return 	render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
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
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
