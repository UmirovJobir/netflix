from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ActorViewSet, MovieActorAPIView, CommentAPIView, CommentDetailAPIView
# from .views import CommentViewSet
# from .views import ActorAPIView, MovieAPIView


router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
# router.register('comments', CommentViewSet, 'comment')

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view()),
    path('auth/', obtain_auth_token),
    path('comment/', CommentAPIView.as_view()),
    path('comment/<int:id>/delete/', CommentDetailAPIView.as_view())
]


# urlpatterns = [
#     path('actors/', ActorAPIView.as_view(), name='actors'),
#     path('movies/', MovieAPIView.as_view(), name='movies')
# ]