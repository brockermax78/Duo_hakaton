from rest_framework import viewsets
from game_shop.models import Games
from .models import Comment, Like, Rating
from rest_framework import status
from .serializers import CommentSerializer, RatingSerializer, LikeSerializer 
from rest_framework.permissions import AllowAny, IsAuthenticated
from game_shop.permissions import IsAdminOrPermissionIsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAdminOrPermissionIsAuthenticated]
            
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminOrPermissionIsAuthenticated]
            
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        
        return super().get_permissions()
    
    
class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
class RatingView(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['POST', 'PATCH'], detail=True)
    def set_rating(self, request, pk=None):
        game = get_object_or_404(Games, slug=pk)
        rating, created = Rating.objects.get_or_create(author=request.user, game=game)
        serializer = RatingSerializer(instance=rating, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()

            if created:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LikeView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
       
    @action(['POST'], detail=True)
    def like(self, request, pk = None):
        game = self.get_object()
        user = request.user
        try: 
            like = Like.objects.get(game=game, author = user)
            like.delete()
            message = 'Dislike'
            status = 204
        except Like.DoesNotExist:
            Like.objects.create(game=game, author=user)
            message = 'Liked'
            status = 201
        return Response(message, status=status)

