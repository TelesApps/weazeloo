from .models import Bookmark
from rest_framework import serializers

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark  # This is the model the serializer is tied to
        fields = '__all__'  # Include all fields in the model