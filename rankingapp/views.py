from rest_framework import viewsets
from .serializers import RankingSerializer
from .models import Ranking

class RankingViewset(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
