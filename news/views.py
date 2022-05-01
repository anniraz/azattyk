from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from news.models import News
from news.models import Category
from django.views.generic import ListView


def news_views(request):
    news_all = News.objects.all()
    category_all=Category.objects.all()
    context={
        'news_all':news_all,
        'category_all':category_all
        }
    return render(request, 'index.html',context=context )


def show_post(request,post_slug):
    post=get_object_or_404(News,url=post_slug)
    # category_all=Category.objects.all()
    # news_all = News.objects.filter(category_id=post_id)
    context={'post':post,'title':post.title,'cat':post_slug}
    return render(request, 'home.html',context=context)
# class ShowPost(ListView):
#     model=News
#     template_name='home.html'
#     context_object_name='post'

# class ShowCategory(ListView):
#     model=Category
#     template_name='index.html'
#     context_object_name='news_all'



def show_category(request,categ_id):
    category_all=Category.objects.all()
    news_all = News.objects.filter(category_id=categ_id)
    context={'category_all':category_all,'news_all':news_all}
    return render(request, 'index.html',context=context)
    # return HttpResponse(f'{categ_id}')

    # posts=News.objects.all()
    # post=get_object_or_404(Category,url=categ_slug)

    # context={'post':post,'posts':posts,'title':'Главная страница','cat':categ_slug}
    # return render(request, 'index.html',context=context)
