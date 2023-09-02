from rest_framework.serializers import ModelSerializer, ValidationError
# <<<<<<< HEAD
# from .models import Games, Category

# class CategorySerializer(ModelSerializer):
    
#     class Meta:
#         model = Category
#         fields = ('title',)
        
# class GameListSerializer(ModelSerializer):
    
#     class Meta:
#         model = Games
#         fields = '__all__'
         
    
        
# =======

'''код сверху закоментирован для решение конфликтов'''
from rest_framework import serializers
from .models import Games, Category
# from review.models import Comment, Like, Rating
# from review.serializers import CommentSerializer
from django.db.models import Avg


class CategorySerializer(ModelSerializer):
    # admin_only = serializers.BooleanField(read_only=True)
    class Meta:
        model = Category
        fields = ['title','slug']
        
        
class GameListSerializer(ModelSerializer):
    admin_only = serializers.BooleanField(read_only=True)    
    class Meta:
        model = Games
        fields = '__all__'
        
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['ratings'] = instance.rating.aggregate(Avg('rating'))['rating__avg']
    #     representation['likes']= instance.like.count()
    #     representation['comments'] = CommentSerializer(Comment.objects.filter(post=instance.pk), many=True).data
    #     return representation 
         

