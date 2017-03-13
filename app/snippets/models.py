from django.db import models

# Create your models here.

class Snippet(models.Model):
    title = models.CharField(max_length=256, blank=False, null=False)
    language = models.CharField(max_length=256, blank=False, null=False)
    snippet = models.TextField(max_length=1000, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)

    def __str__(self):
        """ returns a human readable version of the student object """
        return 'Title: {0}\n  Language: {1}\n Snippet: {2}\n Description: {3}\n'.format(self.title, self.language, self.snippet, self.description)
        