from django.db import models

# Create your models here.

class Players(models.Model):
    player_name = models.CharField(max_length=25)
    character_name = models.ForeignKey(CharacterStats, on_delete=models.CASCADE)
    status = models.BooleanField()
    e_mail = models.EmailField()

class CharacterStats(models.Model):
    character_name = models.ForeignKey(CharacterStory, on_delete=models.CASCADE)
    test = models.IntegerField()
    lelek = models.IntegerField()

    elme = models.IntegerField()
    elet = test * 2
    akarat = lelek + elme

    vegzet = models.IntegerField()
    varazs = vegzet + 9
    tisztanlatas = models.IntegerField()


class CharacterStory(models.Model):
    character_name = models.CharField(max_length=25)
    lost = models.DateField()
    found = models.DateField()
    seeming_kith = models.CharField(max_length=25)
    elrablo = models.CharField(max_length=25)
    udvar =models.ForeignKey(Udvarok, on_delete=models.CASCADE)
    uralkodo = models.BooleanField()


class CharacterMagic(models.Model):
    character_name = models.ForeignKey(CharacterStats, on_delete=models.CASCADE)
    magic_name = models.ForeignKey(Contracts, on_delete=models.CASCADE)


class CharacterSkillsBackgrounds(models.Model):
    character_name = models.ForeignKey(CharacterStory, on_delete=models.CASCADE)
    skill_background_name = models.ForeignKey


class SkillsBackgrounds(models.Model):
    name = models.CharField(max_length=25)
    tipus = models.Field.choices(('skill'), ('background'))
    magical = models.BooleanField()
    clarity_related = models.BooleanField()
    description = models.TextField()


class Contracts(models.Model):
    name = models.CharField(max_length=25)
    tipus = models.Field.choices(('court'), ('general'), ('egyedi'))
    description = models.TextField()


class Pledges(models.Model):
    character_name = models.ForeignKey(CharacterStory, on_delete=models.CASCADE)
    pledge_name = models.CharField(max_length=25)
    tipus = models.CharField(max_length=25) # eg. city, click, etc.
    start = models.TimeField()
    end = models.TimeField()
    duration = models.Field.choices(('napszak'), ('haromnap'), ('honap'), ('evszak'), ('ev'), ('halalig'), ('orokke')) #kellenek majd a szamok melle
    duration_metrics = models.IntegerField()
    description = models.TextField()
    boon = models.CharField(max_length=25)
    boon_metrics = models.IntegerField()
    curse = models.CharField(max_length=25)
    curse_metrics = models.IntegerField()


class Udvarok(models.Model):
    court_name = models.CharField(max_length=10)
    court_contracts = models.ForeignKey(Contracts, on_delete=models.CASCADE)
    uralkodo = models.ForeignKey(CharacterStory, on_delete=models.CASCADE))
    description = models.TextField()