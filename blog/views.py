from django.shortcuts import render,HttpResponse

from blog.models import Blog

# Create your views here.
def single_blog(request,pk):
    try:
        b = Blog.objects.get(id=pk)
    except:
        return HttpResponse('page not found!!!')
    return render(request ,'single_blog.html',{'blog':b})

def home(req):
    return render(req,'home.html')

def blog_home(req):
    blogs_objects = Blog.objects.all()
    context_dict = {'name':'anup','blogs':blogs_objects}
    
    return render(req , 'blog_home.html', context_dict)

def comment_view(request):
    return HttpResponse('COMMENT')

def media_view(request):
    return HttpResponse('MEDIA')

def account_view(request):
    return HttpResponse('ACCOUNT')


def html_views(req):
    return render(req,'demo.html')