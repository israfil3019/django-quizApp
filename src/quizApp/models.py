from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=30)  
    category = models.ForeignKey(Category, related_name="quiz", on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)
    def __str__(self):
        return self.title


class Question(models.Model):
    OPTIONS = (
        ('1', 'Easy'),
        ('2', 'Intermediate'),
        ('3', 'Difficult')
    )

    question_text = models.CharField(max_length=200)  
    quiz = models.ForeignKey(Quiz, related_name="questions", on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=15, choices=OPTIONS, default='Easy')
    created_date = models.DateTimeField(
        default=timezone.now)
    def __str__(self):
        return self.question_text

class Choice(models.Model):

    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question} -- {self.id}"
