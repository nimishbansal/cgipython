from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from main_app.api.serializers import GameSerializer, GamePlatformSerializer, GameGenreSerializer
from main_app.models import Game, GamePlatform, GameGenre


class StandardPagination(PageNumberPagination):
    page_size = 10


class GamesListAPIView(ListAPIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = GameSerializer
    pagination_class = StandardPagination

    def get(self, request, *args, **kwargs):
        res = super(GamesListAPIView, self).get(request, *args, **kwargs)
        platforms = GamePlatformSerializer(GamePlatform.objects.all(), many=True)
        genres = GameGenreSerializer(GameGenre.objects.all(), many=True)
        editors_choice = ['Y', 'N']
        res.data.update({"platforms": platforms.data})
        res.data.update({"genres": genres.data})
        res.data.update({"editors_choice": editors_choice})
        return res

    def get_queryset(self):
        queryset = Game.objects.all()
        return queryset


class GameDetailAPIView(RetrieveAPIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
