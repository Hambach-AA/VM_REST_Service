from django.db import models
from django.forms import ModelForm

from GameMap.models import Location

Choices_class = (
    ('Knight', u'Knight'),
    ('Wizard', u'Wizard'),
    ('Thief', u'Thief'),
    ('Paladin', u'Paladin'))

class Player(models.Model):
    name = models.CharField(verbose_name=u'User Name', max_length=30, blank=True)
    playerclass = models.CharField(verbose_name=u'Player Class', max_length=15, choices=Choices_class, default='Knight')
    email = models.CharField(verbose_name=u'Email', max_length=50, blank=True)
    level = models.IntegerField(verbose_name=u'Player Level', default=0)
    position = models.ForeignKey(Location, default=1, on_delete=models.SET_DEFAULT)

    def __unicode__(self):
        return self.name


