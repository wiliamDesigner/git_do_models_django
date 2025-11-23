from django.db import models

class Pessoa(models.Model):
    nome=models.CharField(max_length=100)
    idade=models.IntegerField()
    rua=models.CharField(max_length=50)
    bairro=models.CharField( max_length=100)
    telefone=models.IntegerField()