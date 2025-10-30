from django.db import models

from django.conf import settings
from django.utils import timezone


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Snippet(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='snippets',
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        Tag, related_name='snippets',
        blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
