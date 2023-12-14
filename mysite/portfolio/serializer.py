from rest_framework import serializers
from .models import Projects, Image


class ImagePortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']



class ProjectsSerializer(serializers.ModelSerializer):
    images = ImagePortfolioSerializer(many=True)
    class Meta:
        model = Projects
        fields = ['name', 'description', 'images']












