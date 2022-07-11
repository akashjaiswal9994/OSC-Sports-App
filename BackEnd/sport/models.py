from django.db import models

# Create your models here.

class Player(models.Model):
    SPORT_TYPE=[
        ('None','NONE' ),
        ('Chess','CHESS' ),
        ('Basket Ball','BASKET BALL' ),
        ('FootBall','FOOTBALL' ),
        ('Cricket','CRICKET' ),
        ('Volley Ball ','VOLLEY BALL' ),
        ('Floor Ball','FLOOR BALL' ),
        ('Table Tennis','TABLE TENNIS'),
        ('MARTIAL ART','MARTIAL ART' ),
        ('Kayaking','Kayaking' ),
        (' Bobsleighing',' Bobsleighing' ),
        (' Canoeing',' Canoeing' ),
        ('Skiing','Skiing' ),
        ('Surfing','Surfing' ), 
        ('Snorkeling','Snorkeling' ), 
        ('Olympic Swimming','Olympic Swimming' )
    ]
    player_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    email=models.EmailField()
    Sport=models.CharField(max_length=50,choices=SPORT_TYPE,default='None')


