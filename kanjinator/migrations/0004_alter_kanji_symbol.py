# Generated by Django 4.1.4 on 2023-01-02 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanjinator', '0003_kanji_jlpt_kanji_grade_kanji_strokes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanji',
            name='symbol',
            field=models.CharField(max_length=5),
        ),
    ]