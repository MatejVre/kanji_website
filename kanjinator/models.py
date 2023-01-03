from django.db import models

# Create your models here.
class Kanji(models.Model):
    symbol = models.CharField(max_length=5)
    strokes = models.IntegerField()
    grade = models.IntegerField()
    kanji_classification = models.CharField(max_length=200)
    JLPT = models.IntegerField()
    radical = models.CharField(max_length=200)
    joyo_reading = models.CharField(max_length=200)
    non_joyo_reading = models.CharField(max_length=200, null=True)
    meaning = models.CharField(max_length=200)
    on_within_joyo = models.CharField(max_length=200)
    kun_within_joyo = models.CharField(max_length=200)