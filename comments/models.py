from django.db import models
from django.db.models import CASCADE
from posts.models import Post
from users.models import User


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=CASCADE)
    post = models.ForeignKey(Post, null=True, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
