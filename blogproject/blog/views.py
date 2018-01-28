from django.shortcuts import render,get_object_or_404

# Create your views here.
#  from django.http import HttpResponse这个其实不怎么用


from .models import Post

def index(request):
    #return render(request,'blog/index.html',context={'title':'蒋爸爸的博客',
                                                     #'welcome':'欢迎欢迎，热烈欢迎！'
                                                     #})
    post_list = Post.objects.filter(is_deleted=False).order_by('-id')
    #post_list = Post.objects.all().order_by('-id')
    #这边排序是拍的展示页面那个文字排序，
    #后台管理的排序：可在admin里那个class下ordering = ('id')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)#后面这个pk是上面def detail(request,pk)
    return render(request, 'blog/detail.html', context={'post': post})
