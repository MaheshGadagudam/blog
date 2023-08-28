from django.shortcuts import render

from blog.models import Blog, Category
from social.models import About


def home(request):
    
    featured_posts=Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published')
    try:
        about=About.objects.get()
    except:
        about=None
    context={
        
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about
    }
    return render(request,'home.html',context)