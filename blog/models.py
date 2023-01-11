from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


# post model
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/')
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager()  # The default manager.
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)


class Flight(models.Model):
    COUNTRY_CHOICES = (
        ('USA', 'USA'),
        ('CHINA', 'CHINA'),
        ('RUSSIA', "RUSSIA"),
        ('INDIA', 'INDIA'),
        ('OTHER', 'OTHER')
    )
    COMPANY_CHOICES = (
        ('SPACEX', 'SPACEX'),
        ('BLUE ORIGIN', 'BLUE ORIGIN'),
        ('ROCKET LAB', "ROCKET LAB"),
        ('NOT COMPANY', "NOT COMPANY")
    )

    flight_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=15, choices=COUNTRY_CHOICES, default='USA')
    company = models.CharField(max_length=15, choices=COMPANY_CHOICES, default='NOT COMPANY')
    date = models.DateTimeField(default=timezone.now)
    upload = models.ImageField(upload_to='logo/')
    succes = models.BooleanField(default=True)
