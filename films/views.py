from django.db.models import Model
from django.shortcuts import render
from rest_framework import status
from rest_framework import filters

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from films.models import Actor, Movie, Comment
from films.serializers import ActorSerializer, MovieSerializer, CommentSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    order_fields = ['imdb', '-imdb']
    search_fields = ['name']
    filterset_fields = ['genre']

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        id = request.data.get('id')
        actor = Actor.objects.get(id=id)
        movie.actors.add(actor)

        serializer = ActorSerializer(actor)
        movie.save()

        return Response(data=serializer.data)

    @action(detail=True, methods=['POST'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        id = request.data.get('id')
        actor = Actor.objects.get(id=id)
        movie.actors.remove(actor)

        serializer = ActorSerializer(actor)
        movie.save()

        return Response(data=serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieActorAPIView(APIView):
    def get(self, request, id):
        movie = Movie.objects.get(pk=id)
        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)

        return Response(serializer.data)


class CommentAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user_id'] = self.request.user
        serializer.save()

        return Response(data=serializer.data)

    def get(self, request):
        comments = Comment.objects.filter(user_id=self.request.user)
        serializer = CommentSerializer(comments, many=True)

        return Response(data=serializer.data)


class CommentDetailAPIView(APIView):
    def delete(self, request, id):
        comment = Comment.objects.get(pk=id)
        comment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)





# class CommentViewSet(ModelViewSet):
#     serializer_class = CommentSerializer
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#
#     def get_queryset(self):
#         return Comment.objects.filter(user_id=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.validated_data['user_id'] = self.request.user
#         serializer.save()


# class ActorAPIView(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ActorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#
#         return Response(data=serializer.data)
#
#
# class MovieAPIView(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#
#         return Response(data=serializer.data)
