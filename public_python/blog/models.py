from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="", upload_to="blog/posts/")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    pub_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
