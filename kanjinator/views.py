from django.shortcuts import render
from django.http import HttpResponse
from django import forms
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
    return render(request, 'kanjinator/jlpt.html', {'chars':list})

def result(request):
    query = request.POST['search']
    option = request.POST['option']
    if option == "reading" and len(query.strip()) != 0:
        kanji = Kanji.objects.filter(joyo_reading__contains= query.strip())
    elif option == "symbol" and len(query.strip()) != 0:
        kanji = Kanji.objects.filter(symbol__exact=query)
    elif option == "grade":
        kanji = Kanji.objects.filter(grade__exact=query)
    else:
        kanji = Kanji.objects.none
    return render(request, 'kanjinator/search.html', {'chars':kanji, 'option':option, 'query':query})