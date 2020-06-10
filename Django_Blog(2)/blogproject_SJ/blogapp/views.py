from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects

    # blog 모든 글을 대상으로
    blog_list = Blog.objects.all()
    # blog 객체 3개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    # request된 페이지가 무엇인지 알아내서 page 변수에 번호 담기
    page = request.GET.get('page')
    # request된 페이지 얻어온 뒤 리턴
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

# new.html을 띄워주는 함수
def new(request):
    return render(request, 'new.html')

# 입력받은 내용을 DB에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()     # DB에 저장
    return redirect('/blog/'+str(blog.id))


def blogpost(request):
    # 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            # post = BLog형 객체 (Model 객체를 리턴하되 저장하지 말아라)
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    
    # 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})