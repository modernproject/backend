from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
