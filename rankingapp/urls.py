from django.urls import path                                                                                           
from django.urls import include                                                                                        
from rankingapp import views                                                                                               
from rest_framework import routers
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'ranking', views.RankingViewset)
                                                                                                                       

urlpatterns = [
    url(r'^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
