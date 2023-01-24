from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Kanji
import random
from django.db.models import Q
from django import template


KANJI_APP_TOKEN = "https://kanjialive-api.p.rapidapi.com/api/public/kanji/"
# Create your views here.
def index(request):
    
    return render(request, 'kanjinator/index.html')

def kanji(request, character):
    char = Kanji.objects.get(kanji=character)
    return render(request, 'kanjinator/kanji.html', {'kanji':char})

def test(request):
    list = Kanji.objects.filter(JLPT__exact=5)
    list2 = []
    for i in list:
        list2.append(i)
    return HttpResponse(list2[6].kanji)

def jlpt(request, level):
    list = Kanji.objects.filter(JLPT__exact=level)
    return render(request, 'kanjinator/jlpt.html', {'chars':list})

def result(request):
    query = request.GET['search']
    option = request.GET['option']
    if option == "reading" and len(query.strip()) != 0:
        kanji = Kanji.objects.filter(Q(kun_readings__contains=query.strip()) | Q(on_readings__contains= query.strip()))
    elif option == "kanji" and len(query.strip()) != 0:
        kanji = Kanji.objects.filter(kanji__in=list(query))
    elif option == "grade":
        kanji = Kanji.objects.filter(grade__exact=query)
    else:
        kanji = Kanji.objects.none
    return render(request, 'kanjinator/search.html', {'chars':kanji, 'option':option, 'query':query})

def practice(request, level):
    list = Kanji.objects.filter(JLPT__exact=level)
    index = random.randint(0, len(list)-1)
    return render(request, 'kanjinator/practice.html', {'kanji':list[index]})

@register.filter
def next(list, current_index):
    try:
        return list[current_index +1]
    except:
        return False;