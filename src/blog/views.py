from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from haystack.generic_views import SearchView
from .models import Post, Series, Category, Topic, Explained, ResourcesTopic, ResourcesContent

def post_list_home(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 4) # posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results 
        posts = paginator.page(paginator.num_pages)

    most_popular = Post.published.filter(most_popular=True)
    recent_posts = Post.published.all().order_by('-published_date')[:4]
    return render(request, 'blog/post_list_home.html', {'posts': posts, 'page': page, 'most_popular': most_popular, 'recent_posts': recent_posts} )

def post_detail(request, category, series, slug):
    post = Post.published.get(slug=slug)
    related_posts = Post.published.filter(series__slug=series).order_by('published_date')
    most_popular = Post.published.filter(most_popular=True)
    recent_posts = Post.published.all().order_by('-published_date')[:4]
    return render(request, 'blog/post_detail.html', {'post': post, 'related_posts': related_posts, 'most_popular': most_popular, 'recent_posts': recent_posts})

def series_list(request, category, series):
    siri = Series.objects.get(slug=series)
    posts = Post.published.filter(series__slug=series).order_by('published_date')
    most_popular = Post.published.filter(most_popular=True)
    recent_posts = Post.published.all().order_by('-published_date')[:4]
    return render(request, 'blog/series_list.html', {'series': siri, 'posts': posts, 'most_popular': most_popular, 'recent_posts': recent_posts})

def archive(request):
    all_series = Series.objects.all().exclude(slug="general")
    all_posts = Post.published.all().order_by('published_date')
    most_popular = Post.published.filter(most_popular=True)
    recent_posts = Post.published.all().order_by('-published_date')[:4]
    return render(request, 'blog/archive.html', {'series': all_series, 'posts': all_posts, 'most_popular': most_popular, 'recent_posts': recent_posts})

def about(request):
    most_popular = Post.published.filter(most_popular=True)
    recent_posts = Post.published.all().order_by('-published_date')[:4]
    return render(request, 'blog/about.html', {'most_popular': most_popular, 'recent_posts': recent_posts})

def resources(request):
    all_explained = Explained.published.all()
    most_popular = Post.published.filter(most_popular=True)
    recent_posts = Post.published.all().order_by('-published_date')[:4]
    resources_topics = ResourcesTopic.objects.all()
    resources_content = ResourcesContent.objects.all()
    return render(request, 'blog/resources.html', {'explained': all_explained, 'most_popular': most_popular, 'recent_posts': recent_posts, 'resources_topics': resources_topics, 'resources_content': resources_content})

def explained(request, slug):
    explained_post = Explained.published.get(slug=slug)
    series = Series.objects.all().exclude(slug="general")
    most_popular = Post.published.filter(most_popular=True)
    recent_posts = Post.published.all().order_by('-published_date')[:4]
    return render(request, 'blog/explained.html', {'post': explained_post, 'series': series, 'most_popular': most_popular, 'recent_posts': recent_posts})

class MySearchView(SearchView):
    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        most_popular = Post.published.filter(most_popular=True)
        recent_posts = Post.published.all().order_by('-published_date')[:4]
        context.update({'most_popular': most_popular, 'recent_posts': recent_posts})
        return context