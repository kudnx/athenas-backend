from django.db import models

# Create your models here.

TIPOLOGIA_CHOICES = [
    ("M", "Masculino"),
    ("F", "Feminino"),
]

class Pessoa(models.Model):

    class Meta:
        db_table = 'pessoa'

    nome = models.CharField(max_length=100)
    data_de_nasc = models.DateField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1, choices=TIPOLOGIA_CHOICES)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
