from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('kanji/<str:character>/', views.kanji, name='kanji'),
    path('JLPT<int:level>', views.jlpt, name='jlpt'),
    path('test', views.test, name="test"),
    path('search/', views.result, name="result"),
    path('practice/N<int:level>', views.practice, name="practice")
]
