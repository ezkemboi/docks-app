from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Template(models.Model):
    slug = models.SlugField(unique=True, primary_key=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    documenttype = models.CharField(max_length=100)
    title = JSONField()
    documentfieldsitems = JSONField()

    class Meta:
        verbose_name = "Template"
        verbose_name_plural = "Templates"

    def __unicode__(self):
        return self.slug
