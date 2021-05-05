from django.db import models

class BlogEntry(models.Model):
    pub_date = models.DateTimeField(null=True) # Null for drafts.
    byline = models.CharField(max_length=100)
    title = models.TextField()
    content = models.TextField()
    abstract = models.TextField()
    is_draft = models.BooleanField()
