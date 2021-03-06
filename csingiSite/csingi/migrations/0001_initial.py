# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterMagic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterSkillsBackgrounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.IntegerField()),
                ('lelek', models.IntegerField()),
                ('elme', models.IntegerField()),
                ('vegzet', models.IntegerField()),
                ('tisztanlatas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CharacterStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_name', models.CharField(max_length=25)),
                ('lost', models.DateField()),
                ('found', models.DateField()),
                ('seeming_kith', models.CharField(max_length=25)),
                ('elrablo', models.CharField(max_length=25)),
                ('uralkodo', models.BooleanField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('tipus', models.CharField(max_length=25)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=25)),
                ('e_mail', models.EmailField(max_length=254)),
                ('character_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csingi.CharacterStory')),
            ],
        ),
        migrations.CreateModel(
            name='Pledges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pledge_name', models.CharField(max_length=25)),
                ('tipus', models.CharField(max_length=25)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('duration', models.CharField(max_length=25)),
                ('duration_metrics', models.IntegerField()),
                ('description', models.TextField()),
                ('boon', models.CharField(max_length=25)),
                ('boon_metrics', models.IntegerField()),
                ('curse', models.CharField(max_length=25)),
                ('curse_metrics', models.IntegerField()),
                ('character_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csingi.CharacterStory')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsBackgrounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('tipus', models.CharField(max_length=25)),
                ('magical', models.BooleanField()),
                ('clarity_related', models.BooleanField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Udvarok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court_name', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('court_contracts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csingi.Contracts')),
            ],
        ),
        migrations.AddField(
            model_name='characterstory',
            name='udvar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csingi.Udvarok'),
        ),
        migrations.AddField(
            model_name='characterstats',
            name='character_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csingi.CharacterStory'),
        ),
        migrations.AddField(
            model_name='characterskillsbackgrounds',
            name='character_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csingi.CharacterStory'),
        ),
        migrations.AddField(
            model_name='charactermagic',
            name='character_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csingi.CharacterStats'),
        ),
        migrations.AddField(
            model_name='charactermagic',
            name='magic_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='csingi.Contracts'),
        ),
    ]
