# Generated by Django 3.2.9 on 2021-12-25 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystudy_app', '0031_auto_20211224_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='discipline_label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mystudy_app.disciplinelabel'),
        ),
    ]
