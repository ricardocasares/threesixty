# Generated by Django 2.0.5 on 2018-07-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threesixty', '0003_auto_20180216_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='show_question_progress',
            field=models.BooleanField(default=False, help_text='', verbose_name='show question progress'),
        ),
    ]
