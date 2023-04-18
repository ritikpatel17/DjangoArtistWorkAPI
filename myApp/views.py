from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Artist, Work
from .serializers import ArtistSerializer, WorkSerializer


from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Work, Artist
from .serializers import ArtistSerializer, WorkSerializer
from .filters import WorkFilter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


    
class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class WorkList(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkFilter

class WorkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

