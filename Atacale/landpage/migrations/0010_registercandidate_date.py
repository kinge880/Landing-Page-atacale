# Generated by Django 4.1.1 on 2022-09-29 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0009_registercandidate_pis'),
    ]

    operations = [
        migrations.AddField(
            model_name='registercandidate',
            name='date',
            field=models.DateField(null=True, verbose_name='Data da inscrição'),
        ),
    ]
