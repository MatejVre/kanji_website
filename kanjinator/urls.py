from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:character>/', views.kanji, name='kanji'),
    path('JLPT<int:level>', views.jlpt, name='jlpt'),
    path('test', views.test, name="test")
]
