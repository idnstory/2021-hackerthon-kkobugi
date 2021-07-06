from rest_framework import viewsets
from .serializers import RankingSerializer
from .models import Ranking
import datetime

class RankingViewset(viewsets.ModelViewSet):
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

    #queryset = Ranking.objects.filter(created__range=(today_min, today_max)).order_by('-score')
    queryset = Ranking.objects.all().order_by('-score')

    serializer_class = RankingSerializer
