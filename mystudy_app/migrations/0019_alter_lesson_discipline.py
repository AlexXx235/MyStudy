# Generated by Django 3.2.9 on 2021-12-22 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystudy_app', '0018_auto_20211222_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='discipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mystudy_app.discipline'),
        ),
    ]
