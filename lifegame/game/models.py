from django.db import models
import json

e = 'enter'
r = 'rejection'
ex = 'exit'
p = 'permanent'
# Create your models here.
def triplet():
    return {e: 0, p: 0, ex: 0}

def stats_default():

    desc = dict()
    desc['Powers']={e:0, r:0, p:0, ex:0}
    desc['Work']=triplet()
    desc['Health']=triplet()
    desc['Finances']=triplet()
    desc['Relations']=triplet()
    desc['Self time']=triplet()
    desc['Self development']=triplet()
    desc['Random enter event']="Script"
    desc['Enter condition']='Script'
    desc['Exit condition']='Script'
    desc["Rotation condition"] = 'Script'
    desc['Additional cards']=0
    desc['ROT_Powers']={e:0, r:0, p:0, ex:0}
    desc['ROT_Work']=triplet()
    desc['ROT_Health']=triplet()
    desc['ROT_Finances']=triplet()
    desc['ROT_Relations']=triplet()
    desc['ROT_Self time']=triplet()
    desc['ROT_Self development']=triplet()
    desc['ROT_Random enter event']="Script"
    desc['ROT_Enter condition']='Script'
    desc['ROT_Exit condition']='Script'
    desc["ROT_Rotation condition"] = 'Script'
    desc['ROT_Additional cards']=0

    return json.dumps(desc)

class Card(models.Model):

    name = models.CharField(max_length=255, help_text="Card name")
    version = models.IntegerField(help_text="Card_version autofill")
    stats = models.JSONField(help_text="Card stats", default=stats_default())
    image = models.ImageField(help_text='Image of card', height_field=890, width_field=570, blank=True)







class Deck(models.Model):

    name = models.CharField(max_length=255, help_text="name deck")
    version = models.IntegerField(help_text="version of deck")
    cards = models.ManyToManyField(Card)


