from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Table(models.Model):
    
    owner = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=200)
    big_blind = models.IntegerField(default=10)
    
class Player(models.Model):
	
	owner = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
	table = models.ForeignKey(Table, default=1, on_delete=models.SET_DEFAULT)
	chips = models.IntegerField(default=1000)
	table = models.ForeignKey(Table, null = True, default=1, on_delete=models.SET_DEFAULT)
	card_1 = models.CharField(max_length=3, null=True)
	card_2 = models.CharField(max_length=3, null=True)
    
    
    
    
    