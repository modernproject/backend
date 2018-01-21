from django.db import models
from django.utils.text import slugify

class Post(models.Model):
    BACKEND = 'BACKEND'
    FRONTEND = 'FRONTEND'
    DEPLOYMENT = 'DEPLOYMENT'

    POST_CATEGORY = (
        (BACKEND, 'Backend'),
        (FRONTEND, 'Frontend'),
        (DEPLOYMENT, 'Deployment'),
    )

    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug = models.SlugField(unique=True, default='default')
    content = models.TextField(blank=False)
    category = models.CharField(max_length=50, choices=POST_CATEGORY, default=BACKEND)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    premium = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
