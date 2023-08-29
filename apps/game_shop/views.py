from rest_framework import generics
from .models import Games, Category
from .serializers import GameListSerializer, CategorySerializer
from .permissions import IsAdminPermision, IsAuthenticated
from rest_framework.decorators import action


class GameListCreateView(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GameListSerializer
    
    @action (methods= ['Post', 'Patch'], detail=True)
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminPermision]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
            
        return super().get_permissions()
    
class GameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GameListSerializer
    
    @action (methods= ['Post', 'Patch'], detail=True)
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminPermision]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
            
        return super().get_permissions()
    
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    