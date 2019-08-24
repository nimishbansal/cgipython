from django.shortcuts import render
# Create your views here.
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from main_app.models import GamePlatform, GameGenre


@api_view(('GET', 'POST'))
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((AllowAny,))
def home(request):
    platforms = GamePlatform.objects.all()
    genres = GameGenre.objects.all()
    editors_choices = ['Y', 'N']
    context = {
        'platforms': platforms,
        'genres': genres,
        'editors_choices': editors_choices
    }
    return render(request, 'main_app/home.html', context=context)
    # return Response('ok')

