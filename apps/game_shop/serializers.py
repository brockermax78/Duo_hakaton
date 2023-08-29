from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Games, Category

class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('title',)
        
class GameListSerializer(ModelSerializer):
    
    class Meta:
        model = Games
        fields = '__all__'
         
    
        