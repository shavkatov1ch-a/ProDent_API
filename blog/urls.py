from django.urls import path
from .views import *
urlpatterns = [
    path('home/', HomeAPIView.as_view(), name='home'),
    path('post/', PostAPIView.as_view(), name='post'),
    path('tag/', TagAPIView.as_view(), name='tags'),
    path('about/', AboutAPIView.as_view(), name='about'),
    path('service/', ServiceAPIView.as_view(), name='service'),
    path('blog/', BlogAPIView.as_view(), name='blog')

]