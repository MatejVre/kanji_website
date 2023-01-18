from django.db import models

# Create your models here.
class Kanji(models.Model):
    kanji = models.CharField(max_length=5)
    grade = models.IntegerField()
    strokes = models.IntegerField()
    meanings = models.CharField(max_length=200)
    kun_readings = models.CharField(max_length=200, null=True)
    on_readings = models.CharField(max_length=200, null=True)
    name_readings = models.CharField(max_length=200, null=True)
    kanji_classification = models.CharField(max_length=200, null=True)
    JLPT = models.IntegerField(null=True)
    
    
    
    