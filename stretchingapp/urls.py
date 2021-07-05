from django.urls import path                                                                                           
from django.urls import include                                                                                        
from stretchingapp import views                                                                                               
                                                                                                                       
urlpatterns = [                                                                                                        
    path('', views.main, name='main'),                                                                               
]                 
