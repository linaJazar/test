
from django.http import HttpResponse
from rest_framework import viewsets
import time

from rest_framework.response import Response

# import local data
from .serializers import GeeksSerializer
from .models import GeeksModel


# create a viewset
class GeeksViewSet(viewsets.ModelViewSet):
    # define queryset

    queryset = GeeksModel.objects.all()


    # specify serializer to be used
    serializer_class = GeeksSerializer


def index(request):
    time.sleep(7)
    return HttpResponse("WAAAAAAAAAAAAAAAAAAAAAAAAIT")
