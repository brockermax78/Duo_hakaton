from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('game_shop', GameRetrieveUpdateDestroyView, basename = 'game_shop')

urlpatterns = [
    path('c-games/', GameListCreateView.as_view()),
    path('rud-games/', GameRetrieveUpdateDestroyView.as_view()),
    path('c-categories/',CategoryListCreateView.as_view()),
    path('rud-categories/',CategoryListCreateView.as_view()),

]