

from django.shortcuts import render
from django.utils import timezone
from .models import Post,Forum

def forum_list(request):
    forums= Forum.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'students_platform/post_list.html', {'forums': forums})

def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'students_platform/post_list.html', {'posts': posts})

	
