from django.db import models
from django.urls import reverse

# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    descripiton = models.TextField()

    def get_absolute_url(self):
        return reverse("quiz_detail", args=(self.id,))
    
    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=200)
    descripiton = models.TextField()
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.title

class Variant(models.Model):
    text = models.TextField()
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='variants')
    checked = models.BooleanField(default=False)