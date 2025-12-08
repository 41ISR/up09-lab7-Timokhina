from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    content = models.TextField()
    tags = models.CharField(max_length=255)
    tags.help_text = "Теги должны разделяться запятой"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title