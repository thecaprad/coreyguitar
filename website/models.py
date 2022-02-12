from tkinter import CASCADE
from django.db import models

class BlogEntry(models.Model):
    date = models.DateField(null=True, blank=True)
    byline = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    abstract = models.TextField()
    is_draft = models.BooleanField()
    slug = models.CharField(max_length=100)

    @property
    def url(self):
        return f'/blog/{self.id}/{self.slug}/'

class Venue(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    street = models.CharField(null=False, blank=False, max_length=50)
    city = models.CharField(null=False, blank=False, max_length=20)
    state = models.CharField(null=False, blank=False, max_length=20)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return "{} — {}, {}".format(
            self.name,
            self.city,
            self.state
        )

class Show(models.Model):
    date = models.DateTimeField(null=False, blank=False)
    description = models.CharField(null=False, blank=False, max_length=100)
    venue = models.ForeignKey(Venue, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "{} — {} @ {}".format(
            self.date.strftime('%x'),
            self.description,
            self.venue.name
        )
