from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(ReadOnlyModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.select_related(
        'team'
    ).all()
    #queryset = Player.objects.all()

    def get_queryset(self):
        query = self.request.query_params.get('query')
        if query:
            qs = super().get_queryset().filter(full_name__icontains=query)
        else:
            qs = super().get_queryset()
        return qs

