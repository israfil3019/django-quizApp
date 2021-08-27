from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    quiz = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = ["id", "name", "quiz"]
