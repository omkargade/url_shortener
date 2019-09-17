from django.urls import path
from shortener.views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', home),
    path('result', short_the_url),
    path('rest/<str:url>',rest_get_post),
    path('<str:short_url>',redirect_url),
]

urlpatterns = format_suffix_patterns(urlpatterns)






