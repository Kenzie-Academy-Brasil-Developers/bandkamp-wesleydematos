from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from albums.models import Album
from .serializers import SongSerializer
from rest_framework import generics


class SongView(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
            album = get_object_or_404(Album, pk=self.kwargs.get('pk'))
            serializer.save(album=album)