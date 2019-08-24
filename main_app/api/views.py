from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from main_app.api.serializers import GameSerializer
from main_app.models import Game


class StandardPagination(PageNumberPagination):
    page_size = 10


class GamesListAPIView(ListAPIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, ]
    serializer_class = GameSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        queryset = Game.objects.all()
        return queryset
