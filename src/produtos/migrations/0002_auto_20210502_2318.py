# Generated by Django 3.2 on 2021-05-03 02:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('codigo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nm_fan', models.CharField(blank=True, max_length=250, null=True)),
                ('nm_emp', models.CharField(blank=True, max_length=200, null=True)),
                ('tp_logr', models.CharField(blank=True, max_length=50, null=True)),
                ('nm_logr', models.CharField(blank=True, max_length=200, null=True)),
                ('nr_logr', models.IntegerField(blank=True, null=True)),
                ('complemento', models.CharField(blank=True, max_length=250, null=True)),
                ('bairro', models.CharField(blank=True, max_length=150, null=True)),
                ('mun', models.CharField(blank=True, max_length=250, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='estabelecimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.estabelecimento'),
        ),
    ]