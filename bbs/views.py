from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm, ArticleForm

#テンプレート(htmlファイル)にデータを送るためのファイル?


def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():#サーチフォームに正しいデータが入っているのなら
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)#Articleの中からフィルターをかける
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()#Articleのすべてのデータを取得
    context = {
            "message" : "Welocom my BBS",
            "articles" : articles,#articleのデータをテンプレートに渡す
            "searchForm" : searchForm,
        }
    return render(request, "bbs/index.html", context)#bbs/index.htmlを表示,第三引数は辞書を用いてテンプレートにデータを渡す
    #テンプレートでは、{{ message }}とするとcontext内のmessageが使用できる


def detail(request, id):
    article = get_object_or_404(Article, pk=id)#Articlの主キーがidのものを取り出す
    context = {
        "message" : "Show Article" + str(id),
        "article" : article
    }
    return render(request, 'bbs/detail.html', context)


def create(request):
    if request.method == "POST":
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid():
            article = articleForm.save()
    context = {
            'message' : "Create article" + str(article.id),
            "article" : article,
        }
    return render(request, "bbs/detail.html", context)


def delete(request, id):
    article = get_object_or_404(Article, pk=id)#Articlの主キーがidのものを取り出す
    article.delete()
    articles = Article.objects.all()
    context = {
        "message" : "Delete Article" + str(id),
        "articles" : articles
    }
    return render(request, 'bbs/index.html', context)


def new(request):
    articleForm = ArticleForm()
    context = {
        "message" : "new Article",
        "articleForm" : articleForm,
    }
    return render(request, "bbs/new.html", context)


def edit(request, id):
    article = get_object_or_404(Article, pk=id)#Articlの主キーがidのものを取り出す
    articleForm = ArticleForm(instance=article)
    context = {
        "message" : "Edit Article" + str(id),
        "article" : article,
        "articleForm" : articleForm,
    }
    return render(request, 'bbs/edit.html', context)


def update(request, id):
    if request.method == "POST":
        article = get_object_or_404(Article, pk=id)#Articlの主キーがidのものを取り出す
        articleForm = ArticleForm(request.POST, instance=article)
        if articleForm.is_valid():
            articleForm.save()
    context = {
        "message" : "Update Article" + str(id),
        "article" : article,
    }
    return render(request, 'bbs/detail.html', context)