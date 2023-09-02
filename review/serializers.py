from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from .models import Like, Rating, Comment

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

    def get_like(self, obj):
        return obj.like.count()

class RatingSerializer(ModelSerializer):
    user = ReadOnlyField(source = 'user.name')
    
    class Meta:
        model = Rating
        fields = '__all__'
        
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        rating = Rating.objects.create(user=user, **validated_data)
        return rating
    
    def validate_rating(self, rating):
        if not 0 <= rating <= 10:
            raise ValidationError('Рейтинг должен быть от 0 до 10')
        return rating
    
    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating')
        instance.save()
        return super().update(instance, validated_data)

class CommentSerializer(ModelSerializer):
    user = ReadOnlyField(source = 'user.name')
    class Meta:
        model = Comment
        fields = '__all__'
        
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        comment = Comment.objects.create(user=user, **validated_data)
        return comment
         