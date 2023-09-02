# <<<<<<< HEAD
# from rest_framework import generics
# from .models import Games, Category
# from .serializers import GameListSerializer, CategorySerializer
# from .permissions import IsAdminPermision, IsAuthenticated
# # from rest_framework.decorators import action
# from rest_framework import viewsets
# import django_filters



# class GameViewSet(viewsets.ModelViewSet):
#     queryset = Games.objects.all()
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

#     filterset_fields = ['tags__slug','category','author']
#     search_fields = ['title','body']
#     ordering_fields = ['created_at','title']



# class GameListCreateView(generics.ListCreateAPIView):
#     queryset = Games.objects.all()
#     serializer_class = GameListSerializer
    
#     # @action(methods= ['Post'], detail=True)
    
#     # def get_permissions(self):
#     #     if self.action in ['create']:
#     #         self.permission_classes = [IsAdminPermision]
#     #     elif self.action in ['list', 'retrieve']:
#     #         self.permission_classes = [IsAuthenticated]
            
#     #     return super().get_permissions()
    


# class GameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Games.objects.all()
#     serializer_class = GameListSerializer
    
#     # @action (methods= ['Get', 'Patch', 'Delete'], detail=True)
    
#     # def get_permissions(self):
#     #     if self.action in ['update', 'partial_update', 'destroy']:
#     #         self.permission_classes = [IsAdminPermision]
#     #     return super().get_permissions()
    

# class CategoryListCreateView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    

# class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
# =======
from rest_framework import generics, permissions, viewsets, filters
from rest_framework.decorators import action
from .models import Games, Category
from review.models import Rating, Like, Comment
from .serializers import GameListSerializer, CategorySerializer
from review.serializers import RatingSerializer, LikeSerializer, CommentSerializer
from .permissions import IsAdminOrReadOnly, IsAuthorPermission
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import django_filters

class GameListCreateView(generics.ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GameListSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return super().get_permissions()

    
class GameRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GameListSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug'

    
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return super().get_permissions()
   
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
       
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'slug' 
    
    

class GameViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rating', 'category']
    search_fields = ['title', 'body']
    ordering_filter = ['created_at', 'title'] 
    
    @action(methods=['POST', 'PATCH'], detail=True)
    def set_reting(self, request, pk=None):
        data = request.data.copy()
        data['games'] = pk
        serializer = RatingSerializer(data=data, context = {'request':request})
        reting = Rating.objects.filter(
            user=request.user, 
            slug=pk
            ).first()
        if serializer.is_valid(raise_exception=True):
            if reting and request.method == 'POST':
                return Response('Reting object exists', status=200)
            elif reting and request.method == 'PATCH':
                serializer.update(reting, serializer.validated_data)
                return Response(serializer.data, status= 200)
            elif request.method == 'POST':
                serializer.create(serializer.validated_data)
                return Response(serializer.data, status= 201)
    
    @action(['POST'], detail=True)
    def like(self, request, pk = None):
        game = self.get_object()
        user = request.user
        try: 
            like = Like.objects.get(game = game, user = user)
            print('=============')
            print(like)
            like.delete()
            message = 'Dislike'
            status = 204
        except Like.DoesNotExist:
            Like.objects.create(game = game, user = user)
            message = 'Liked'
            status = 201
        return Response(message, status=status)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return GameListSerializer
        return GameListSerializer    
    
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
            
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]
            
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        
        return super().get_permissions()
