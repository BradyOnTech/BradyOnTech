from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class ResourcesTopic(models.Model):
    title = models.CharField(max_length=250)
    icon_name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Resources Topic"

    def __str__(self):
        return self.title

class ResourcesContent(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    description = models.TextField()
    topic = models.ForeignKey(ResourcesTopic, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Resources Content"

    def __str__(self):
        return self.name

class Explained(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status= models.CharField(max_length=10,
                             choices=STATUS_CHOICES,
                             default='draft')
    published = PublishedManager()
    slug = models.SlugField(max_length=100)
    
    class Meta:
        ordering = ('-published_date',)
        verbose_name_plural = "Explained"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:explained', args=[self.slug])

class Topic(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="series", default="default.jpg")
    alter_img_url = models.CharField(max_length=350)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:series_list', args=[self.category.slug, self.slug])

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status= models.CharField(max_length=10,
                             choices=STATUS_CHOICES,
                             default='draft')
    published = PublishedManager()
    slug = models.SlugField(max_length=100)
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null="posts")
    most_popular = models.BooleanField(default=False)

    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.series.category.slug,
                                                 self.series.slug,
                                                 self.slug])
