from django.contrib import admin

from .models import Category, Choice, Question, Quiz


admin.site.register(Category)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Quiz)
