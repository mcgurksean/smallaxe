from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.http import HttpResponse

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def thoughts(request):
    return render(request, 'blog/_base.html')

def links(request):
    return render(request, 'blog/links.html')

def projects(request):
    return render(request, 'blog/projects.html')

def cv(request):
    image_data = open('blog/static/pdf/sean_mcgurk_cv_no_contact_details.pdf', 'rb').read()
    return HttpResponse(image_data, content_type='application/pdf')

def header(request):
    return render(request, 'blog/header.html')

def content(request):
    return render(request, 'blog/content.html')

def responsive(request):
    return render(request, 'blog/responsive.html')

def basic(request):
    return render(request, 'blog/_base.html')

def basic_with_responsive_header(request):
    return render(request, 'blog/basic_with_responsive_header.html')

def basic_with_django_girls_content(request):
    return render(request, 'blog/basic_with_django_girls_content.html')
