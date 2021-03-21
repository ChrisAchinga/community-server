from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingPage, name='home'),
    # Aabout page
    path('about/', views.AboutPage, name='about'),
    # tags urls
    path('tags/', views.TagList, name='tags'),
    path('tag/<int:pk>/', views.TagView, name='tag-detail'),
    # images urls
    path('images/', views.ImageList, name='images'),
    # magazine issue urls
    path('magazines/', views.MagazineList, name='magazine'),
    # news
    path('news/', views.AllNewsPage, name='news'),
    path('news/<slug:slug>/', views.NewsReadView.as_view(), name='news-read'),
    # articles
    path('articles/', views.AllArticlesPage, name='articles'),
    path('article/<int:pk>/', views.ArticleReadView.as_view(), name='article-read'),
    # pricing 
    path('pricing/', views.Pricing, name='pricing'),

    # test urls
    path('articles/all', views.ArticleList, name='all-articles'),
    path('news/all', views.NewsList, name='all-news'),
    path('home/', views.TestLanding, name='home-new'),
    path('terms-and-conditions/', views.TermsView, name='terms'),
    path('privacy-policy/', views.PolicyView, name='policy'),
    path('buying-an-issue/', views.ProcedureView, name='procedure'),
    path('create-article/', views.AddArticle, name='new-article'),
]
