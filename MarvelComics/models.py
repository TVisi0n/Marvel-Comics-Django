from django.db import models

class Comic(models.Model):
    name = models.CharField(max_length=100)
    issue = models.CharField(max_length=100)
    description = models.TextField(max_length=300, default="", blank=True)

    addComics = models.Manager()

    def __str__(self):
        return self.issue + ' ' + self.name
