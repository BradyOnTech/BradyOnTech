from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list_home, name='post_list'),
    path('blog/over-explained/<str:slug>', views.explained, name="explained"),
    path('blog/<str:category>/<str:series>/<str:slug>', views.post_detail, name='post_detail'),
    path('blog/<str:category>/<str:series>', views.series_list, name='series_list'),
    path('blog/archive/', views.archive, name='archive'),
    path('about', views.about, name='about'),
    path('resources', views.resources, name='resources'),
    path('search/', views.MySearchView.as_view(), name="search"),
]