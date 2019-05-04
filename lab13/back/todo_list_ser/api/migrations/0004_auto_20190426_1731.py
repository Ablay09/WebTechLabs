# Generated by Django 2.2 on 2019-04-26 11:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20190422_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklist',
            options={'verbose_name': 'TaskList', 'verbose_name_plural': 'TaskLists'},
        ),
        migrations.AddField(
            model_name='tasklist',
            name='created_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 17, 31, 2, 243565)),
        ),
    ]