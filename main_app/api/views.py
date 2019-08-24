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

    def get_queryset(self):
        queryset = Game.objects.all()
        platforms = self.request.query_params.get('platforms')
        editors_choice = self.request.query_params.get('editors_choice')
        genres = self.request.query_params.get('genres')
        search_term = self.request.query_params.get('search_term')
        if platforms:
            queryset = queryset.filter(platform__id__in=platforms.split(","))
        if genres:
            queryset = queryset.filter(genre__id__in=genres.split(","))
        if editors_choice:
            queryset = queryset.filter(editors_choice__in=editors_choice.split(","))
        if search_term:
            queryset = queryset.filter(title__icontains=search_term)

        return queryset.distinct()



class GameDetailAPIView(RetrieveAPIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = GameSerializer
    queryset = Game.objects.all()
