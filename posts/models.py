from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='posts/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=SET_NULL)

    def __str__(self):
        return self.title