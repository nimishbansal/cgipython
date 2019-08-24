from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes

# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from main_app.models import Sample


@api_view(('GET', 'POST'))
@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated, ))
def home(request):
    image = Sample.objects.first().a
    return render(request, 'main_app/home.html', {'file': image})
    # return Response('ok')
