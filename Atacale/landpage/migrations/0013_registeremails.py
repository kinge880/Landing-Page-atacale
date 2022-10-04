# Generated by Django 4.1.1 on 2022-10-04 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landpage', '0012_alter_gerenciadevagas_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerEmails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=255, verbose_name='Destino')),
                ('subject', models.CharField(max_length=255, verbose_name='Título')),
                ('emailId', models.IntegerField(verbose_name='idcandidato')),
                ('body', models.TextField(verbose_name='corpoemail')),
            ],
            options={
                'verbose_name_plural': 'Registro de emails',
            },
        ),
    ]
