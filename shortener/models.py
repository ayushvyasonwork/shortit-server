from django.db import models
import uuid
class ShortURL(models.Model):
    slug = models.CharField(max_length=64, unique=True)
    target = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    visits = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.slug} -> {self.target}"
