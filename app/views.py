from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.
# landing page view
def LandingPage(request):
    small_add = smallAdd.objects.all()
    large_add = largeAdd.objects.all()
    tags = Tag.objects.all()[:5]
    featured_articles = Article.objects.filter(article_feature='featured').order_by('-date')
    news = News.objects.filter(news_feature='featured').order_by('-date')
    context = {'tags':tags, 'featured_articles':featured_articles, 'news':news, 'small_add':small_add, 'large_add':large_add}
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

# view tag
class TagDetail(generic.DetailView):
    model = News
    template_name = 'tags/details.html'

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
    template_name = 'articles/read.html'

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