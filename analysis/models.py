from django.db import models

class Cngm(models.Model):
    id = models.IntegerField()
    nome = models.CharField(max_length=255)
    uri = models.CharField(max_length=255)
    siglaPartido = models.CharField(max_length=10)
    uriPartido = models.CharField(max_length=255)
    siglaUf = models.CharField(max_length=2)
    idLegislatura = models.IntegerField()
    urlFoto = models.CharField(max_length=255)
    email = models.EmailField()

    def __init__(self):
        pass

    def __str__(self):
        return self.nome
