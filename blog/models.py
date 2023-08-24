import uuid
from django.urls import reverse
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class PublishManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = 'PB', "Published"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = RichTextField()
    publish = models.DateTimeField(default=timezone.now)
    banner = models.ImageField(upload_to='blog/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishManager()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"]),
        ]

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    