from django.db import models

class Alunos(models.Model):
    id=models.ObjectIdField()
    nome=models.CharField(max_length=150)
    sobrenome=models.CharField(max_length=150)
    secao=models.CharField(max_length=150)
