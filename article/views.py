from django.shortcuts import render,redirect
from .form import *
from .models import *
from .form import ArticleForms
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    all_article=Article.objects.all()

    paginator=Paginator(all_article,8)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    recent_articles = Article.objects.all().order_by('-pub_date')[:4]
    context={
        # "articles":all_article,
        'page_obj':page_obj,
        "recent_articles":recent_articles
    }
    return render(request,'article/index.html',context)

def single_article(request,pk):
    article=Article.objects.get(pk=pk)
    context={
        'article':article
    }
    return render(request,'article/article.html',context)


def categories(request):
    categories=Category.objects.all()
    print(categories)
    return {'categoreis':categories}

def serach_article(request):
    if 'query' in request.GET:
        query=request.GET['query']
        articles=Article.objects.filter(title__icontains=query)|Article.objects.filter(content__icontains=query)
    context={
        'articles':articles,
        'query':query
    }
    return render(request,'article/categoriesd.html',context)


def categorised_articles(request,pk):
    if pk==0:
        articles=Article.objects.all()
        context = {
            'articles': articles, 
            'category' : 'all' 
            } 
    else:
        category = Category.objects.get(pk=pk)
        articles = Article.objects.filter(category=category).all() 
        print(articles)
        context = {
            'articles':articles,
            'category':category,
        }
    return render(request,'article/categoriesd.html',context)

@login_required
def post_article(request): 
    form = ArticleForms()
    if request.method == "POST":
        form = ArticleForms(request.POST, request.FILES)  
        if form.is_valid():
            article=form.save(commit=False)
            article.author=request.user
            article.save()
            return redirect('article:single_article', pk=form.instance.id) 

    context = {
        'form' : form
    } 
    return render(request, 'article/article_form.html', context) 


class update_article(UpdateView):
    model = Article
    form_class=ArticleForms
    template_name_suffix = "_update"

class DeleteArticle(DeleteView):
    model = Article
    # template_name='templates/article/artcile_delete.html' 
    success_url = reverse_lazy('profile') 


def watchlist(request):
    watchlist_items = WatchlistItem.objects.filter(user=request.user)
    context={
            'watchlist_items': watchlist_items
    }
    return render(request, 'article/watchlist.html',context)

def add_watchlist(request,pk):
    if request.method == 'POST':
        article = request.POST.get('article')
        article= Article.objects.get(pk=pk)
        WatchlistItem.objects.create(user=request.user,article=article)
        WatchlistItem.save()
        return redirect('article:watchlist')
    
def remove_watchlist(request,pk):
    WatchlistItem.objects.filter(pk=pk, user=request.user).delete()
    return redirect('article:watchlist')


