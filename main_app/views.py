from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes

# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from main_app.models import Game


@api_view(('GET', 'POST'))
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated, ))
def home(request):
    a = Game.objects.first()
    return render(request, 'main_app/home.html')
    # return Response('ok')
