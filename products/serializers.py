from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'image', 'username', 'created_at', 'updated_at']

    def create(self, validated_data):
        # 'author' 필드를 validated_data에서 제거
        validated_data.pop('author', None)
        return super().create(validated_data)
