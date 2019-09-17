from django.shortcuts import render, redirect, get_object_or_404
from .models import Shorted
from .utils import create_short
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ShortedSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def rest_get_post(request, url):
    if request.method == 'GET':
        urls = get_object_or_404(Shorted,short_url=url)
        serializer = ShortedSerializer(urls)
        return Response(serializer.data)

    if request.method == 'POST':
        Shorted_obj = Shorted()
        Shorted_obj.url = url
        Shorted_obj.short_url = create_short()
        Shorted_obj.save()
        return Response({"short_url":Shorted_obj.short_url,
                         "url":url
                         },status.HTTP_201_CREATED)


def redirect_url(request, short_url):
    url = get_object_or_404(Shorted, short_url=short_url)
    return redirect("//"+str(url))


def short_the_url(request):
    if request.POST['url'] is None or request.POST['url']=="":
        return render(request,'index.html',{'check': 'Enter a url'})
    Shorted_obj = Shorted()
    Shorted_obj.url = request.POST['url']
    short_url = create_short()
    Shorted_obj.short_url = short_url
    Shorted_obj.save()
    short_url = "Shorted URL: localhost:8000/"+short_url
    return render(request,'result.html',{'result': short_url})


def home(request):
    return render(request, 'index.html',{'check':''})
