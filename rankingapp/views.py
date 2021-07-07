from rest_framework import viewsets, mixins, status
from rest_framework.viewsets import GenericViewSet
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import RankingSerializer
from .models import Ranking
import datetime

class RankingViewset(viewsets.ModelViewSet):
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)

    #queryset = Ranking.objects.filter(created__range=(today_min, today_max)).order_by('-score')
    queryset = Ranking.objects.all().order_by('-score')

    serializer_class = RankingSerializer

class RankingViewsetTest(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    def create(self, request: Request, *args, **kwargs) -> Response:
        dict = {
            "test": "successTest post"
        }
        return Response(dict, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs) -> Response:
        dict = {
            "test": "successTest get"
        }
        return Response(dict, status=status.HTTP_200_OK)





