from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentView #, RatingView, LikeView

router = DefaultRouter()
router.register('comments', CommentView)
# router.register(r'ratings', RatingView)
# router.register(r'likes', LikeView)

urlpatterns = [
    # path('likes/<slug>', LikeView.as_view()),
    # path('ratings/<slug>', RatingView.as_view()),
    # path('comments/<slug>', CommentView.as_view()),
    path('', include(router.urls)),
]