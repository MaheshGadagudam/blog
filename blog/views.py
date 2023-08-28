from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Blog, Category

def posts_by_category(request,category_id):
    posts=Blog.objects.filter(status='Published',category=category_id)
    #try:
        #category=Category.objects.get(pk=category_id)
    #except:
        #return redirect('home')
    category=get_object_or_404(Category,pk=category_id)
    context={
        'posts':posts,
        'category':category
    }
    return render(request,'posts_by_category.html',context)

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug,status='Published')
    context={
        'single_blog':single_blog
    }
    return render(request,'blogs.html',context)