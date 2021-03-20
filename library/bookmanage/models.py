from django.db import models

# Create your models here.
class Book(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = "图书"
        verbose_name_plural = "图书s"