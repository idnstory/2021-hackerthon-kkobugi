from django.urls import path                                                                                           
from django.urls import include                                                                                        
from helloworld import views                                                                                               
                                                                                                                       
urlpatterns = [                                                                                                        
    path('', views.hello, name='hello'),                                                                               
    path('index', views.index, name='index'),                                                                       
    path('camera', views.camera, name='camera'),                                                                       
    path('test', views.test, name='test'),                                                                       
]                 
