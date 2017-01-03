from django.db import models

# Create your models here.

class Contracts(models.Model):
    name = models.CharField(max_length=25)
    tipus = models.CharField(max_length=25) # (('court'), ('general'), ('egyedi'))
    description = models.TextField()

    def __str__(self):
        return self.name


class Udvarok(models.Model):
    court_name = models.CharField(max_length=10)
    court_contracts = models.ForeignKey(Contracts, on_delete=models.CASCADE)
#    uralkodo = models.ForeignKey(CharacterStory, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return self.court_name


class Players(models.Model):
    player_name = models.CharField(max_length=25)
    character_name = models.CharField(max_length=25)
    e_mail = models.EmailField()

    def __str__(self):
        return self.player_name + " " + self.character_name + " " + self.e_mail

class CharacterStory(models.Model):
    character_name = models.ForeignKey(Players, on_delete=models.CASCADE)
    lost = models.DateField()
    found = models.DateField()
    seeming_kith = models.CharField(max_length=25)
    elrablo = models.CharField(max_length=25)
    udvar =models.ForeignKey(Udvarok, on_delete=models.CASCADE)
    uralkodo = models.BooleanField()
    status = models.BooleanField()

    def __str__(self):
        return self.character_name

class CharacterStats(models.Model):
    def elet(self):
        return self.test * 2

    def akarat(self):
        return self.lelek + self.elme

    def varazs(self):
        return self.vegzet + 9

    character_name = models.ForeignKey(CharacterStory, on_delete=models.CASCADE)
    test = models.IntegerField()
    lelek = models.IntegerField()

    elme = models.IntegerField()
    elet = property(elet)
    akarat = property(akarat)

    vegzet = models.IntegerField()
    varazs = property(vegzet)
    tisztanlatas = models.IntegerField()

    def __str__(self):
        return self.character_name


class CharacterMagic(models.Model):
    character_name = models.ForeignKey(CharacterStats, on_delete=models.CASCADE)
    magic_name = models.ForeignKey(Contracts, on_delete=models.CASCADE)

    def __str__(self):
        return self.character_name

class CharacterSkillsBackgrounds(models.Model):
    character_name = models.ForeignKey(CharacterStory, on_delete=models.CASCADE)
    skill_background_name = models.ForeignKey

    def __str__(self):
        return self.character_name

class SkillsBackgrounds(models.Model):
    name = models.CharField(max_length=25)
    tipus = models.CharField(max_length=25) #(('skill'), ('background'))
    magical = models.BooleanField()
    clarity_related = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Pledges(models.Model):
    character_name = models.ForeignKey(CharacterStory, on_delete=models.CASCADE)
    pledge_name = models.CharField(max_length=25)
    tipus = models.CharField(max_length=25) # eg. city, click, etc.
    start = models.TimeField()
    end = models.TimeField()
    duration = models.CharField(max_length=25) #(('napszak'), ('haromnap'), ('honap'), ('evszak'), ('ev'), ('halalig'), ('orokke')) #kellenek majd a szamok melle
    duration_metrics = models.IntegerField()
    description = models.TextField()
    boon = models.CharField(max_length=25)
    boon_metrics = models.IntegerField()
    curse = models.CharField(max_length=25)
    curse_metrics = models.IntegerField()

    def __str__(self):
        return self.character_name

