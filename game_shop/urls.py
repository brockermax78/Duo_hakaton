from django.urls import path, include
# from .views import *
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('game_shop', GameRetrieveUpdateDestroyView, basename = 'game_shop')

# urlpatterns = [
#     path('c-games/', GameListCreateView.as_view()),
#     path('rud-games/', GameRetrieveUpdateDestroyView.as_view()),
#     path('c-categories/',CategoryListCreateView.as_view()),
#     path('rud-categories/',CategoryListCreateView.as_view()),

# ]
# =======

'''код сверху закоментирован для решение конфликтов'''
from game_shop.views import *
from rest_framework.routers import DefaultRouter
from .views import GameViewSet

router = DefaultRouter()
router.register('games',  GameViewSet, basename= 'games')

urlpatterns = [
    path('c-games/', GameListCreateView.as_view()),
    path('rud-games/<slug>/', GameRetrieveUpdateDestroyView.as_view()),
    path('c-categories/',CategoryListCreateView.as_view()),
    path('rud-categories/<slug>/',CategoryRetrieveUpdateDestroyView.as_view()),  
    
    path('', include(router.urls))  
]


