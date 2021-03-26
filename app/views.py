from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import ArticleForm
from django.shortcuts import redirect

# Create your views here.
# landing page view
def LandingPage(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    tags = Tag.objects.all()
    featured_articles = Article.objects.filter(article_feature='featured').order_by('-date')
    latest_news = News.objects.order_by('-id')[0]
    news = News.objects.filter(news_feature='featured').order_by('-date')[:3]
    context = {'tags':tags, 'featured_articles':featured_articles, 'news':news, 'small_add':small_add, 'large_add':large_add, 'latest_news':latest_news}
    return render(request, 'index.html', context)

# about page view
def AboutPage(request):
    return render(request, 'about.html')

# view all Tags
# view all Tags
def TagList(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    tags = Tag.objects.all()
    context = {'tags':tags, 'small_add':small_add, 'large_add':large_add}
    return render(request, 'tags/list.html', context)

# view all magazine issue
def MagazineList(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    magazines = Magazine.objects.all()
    context = {'magazines':magazines, 'small_add':small_add, 'large_add':large_add}
    return render(request, 'magazine/list.html', context)

# view all news
def AllNewsPage(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    tags = Tag.objects.all()[:5]
    news = News.objects.all()
    context = {'news':news, 'tags':tags, 'small_add':small_add, 'large_add':large_add}
    return render(request, 'news/list.html', context)

# news page view
class NewsReadView(generic.DetailView):
    model = News
    template_name = 'news/read.html'

# view all articles view
def AllArticlesPage(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    tags = Tag.objects.all()[:5]
    articles = Article.objects.all()
    context = {'articles':articles, 'tags':tags, 'small_add':small_add, 'large_add':large_add}
    return render(request, 'articles/list.html', context)

# article page view
class ArticleReadView(generic.DetailView):
    model = Article
    template_name = 'articles/new_read.html'

# view all images
def ImageList(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    images = ImageGallery.objects.all()
    context = {'images':images, 'small_add':small_add, 'large_add':large_add}
    return render(request, 'gallery/list.html', context)

# price list view page
def Pricing(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    context = {'small_add':small_add, 'large_add':large_add}
    return render(request, 'accounts/pricing.html', context)


# test pages views

# view all articles view
def ArticleList(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    tags = Tag.objects.all()[:5]
    articles = Article.objects.all()
    context = {'articles':articles, 'tags':tags, 'small_add':small_add, 'large_add':large_add}
    return render(request, 'articles/new_list.html', context)


# article page view
def ArticleView(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    tags = Tag.objects.all()[:5]
    articles = Article.objects.all()
    context = {'articles':articles, 'tags':tags, 'small_add':small_add, 'large_add':large_add}
    return render(request, 'articles/new_read.html', context)

# view all news
def NewsList(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    tags = Tag.objects.all()[:5]
    news = News.objects.all()
    context = {'news':news, 'tags':tags, 'small_add':small_add, 'large_add':large_add}
    return render(request, 'news/new_list.html', context)

def TagView(request, cats):
    cat = str(cats)
    tags = Tag.objects.all()
    tag_posts = Article.objects.filter(tag__name=cat.replace('-', ' ' ))
    context = {'cat':cat.title().replace('-', ' ' ), 'tag_posts':tag_posts, 'tags':tags}
    return render(request, 'tags/details.html', context)

# landing page view
def TestLanding(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    tags = Tag.objects.all()
    featured_articles = Article.objects.filter(article_feature='featured').order_by('-date')
    latest_news = News.objects.order_by('-id')[0]
    news = News.objects.filter(news_feature='featured').order_by('-date')[:3]
    context = {'tags':tags, 'featured_articles':featured_articles, 'news':news, 'small_add':small_add, 'large_add':large_add, 'latest_news':latest_news}
    return render(request, 'new_index.html', context)

# terms and conditions
def TermsView(request):
    return render(request, 'terms.html')

# privacy policy
def PolicyView(request):
    return render(request, 'policy.html')

# procedure for purchasing an issue
def ProcedureView(request):
    return render(request, 'buying-process.html')

# add article
def AddArticle(request):
    form = ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('article')
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'articles/add.html', context)