from django.db import models

# Create your models here.

class Players(models.Model):
    player_name = models.CharField(max_length=25)
    character_name = models.ForeignKey(CharacterStats, on_delete=models.CASCADE)
    status = models.BooleanField()
    e_mail = models.EmailField()

class CharacterStats(models.Model):
    name = models.CharField(max_length=25)
    test = models.IntegerField()
    lelek = models.IntegerField()

    elme = models.IntegerField()
    elet = test * 2
    akarat = lelek + elme

    vegzet = models.IntegerField()
    varazs = vegzet + 9
    tisztanlatas = models.IntegerField()


class CharacterStory(models.Model):
    lost = models.DateField()
    found = models.DateField()
    seeming_kith = models.CharField()
    elrablo = models.CharField()
    

class CharacterSkillsBackgrounds(models.Model):
    name = models.ForeignKey()
    skill_background_name = models.ForeignKey


class SkillsBackgrounds(models.Model):
    name = models.CharField(max_length=25)
    type = models.Field.choices(('skill'), ('background'))
    description = models.TextField()


