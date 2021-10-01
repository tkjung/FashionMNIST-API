from rest_framework import serializers
from .models import Image
class image_serializers(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Image
        fields = ('title', 'image')