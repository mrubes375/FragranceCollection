# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-16 05:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Base_Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Heart_Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Top_Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='fragrance',
            name='fragrance_name',
        ),
        migrations.AddField(
            model_name='fragrance',
            name='house',
            field=models.CharField(default='House', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fragrance',
            name='name',
            field=models.CharField(default='Name', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fragrance',
            name='perfumer',
            field=models.CharField(default='Perfumer', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fragrance',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='top_note',
            name='fragrance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Fragrance'),
        ),
        migrations.AddField(
            model_name='heart_note',
            name='fragrance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Fragrance'),
        ),
        migrations.AddField(
            model_name='base_note',
            name='fragrance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Fragrance'),
        ),
    ]
