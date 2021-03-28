from django.shortcuts import render

# Create your views here.

def blog(request):
    blogs="my blogs"
    return render(request,"blog/blog.html",{"blogs":blogs})