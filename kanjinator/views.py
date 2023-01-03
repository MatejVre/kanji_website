from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
from .models import Kanji

KANJI_APP_TOKEN = "https://kanjialive-api.p.rapidapi.com/api/public/kanji/"
# Create your views here.
def index(request):
    
      
    return render(request, 'kanjinator/index.html')

def kanji(request, character):
    char = Kanji.objects.get(symbol=character)
    return render(request, 'kanjinator/kanji.html', {'kanji':char})

def test(request):
    list = Kanji.objects.filter(JLPT__exact=5)
    list2 = []
    for i in list:
        list2.append(i)
    return HttpResponse(list2[6].symbol)

def jlpt(request, level):
    list = Kanji.objects.filter(JLPT__exact=level)
    characters = list
      
    return render(request, 'kanjinator/jlpt.html', {'chars':characters})