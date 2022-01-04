from django.db import models

class BlogEntry(models.Model):
    date = models.DateField(null=True, blank=True)
    byline = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    abstract = models.TextField()
    is_draft = models.BooleanField()
