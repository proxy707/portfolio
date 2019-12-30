from django.shortcuts import render,get_object_or_404
from .models import Blog

def allblogs(request):
    bl=Blog.objects
    return render(request,'blogs/allblogs.html',{'blo':bl}) 

def detail(request,blog_id):
    detailblog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blogs/detail.html',{'blog':detailblog})