from django.db import models
from uuid import uuid4

# Create your models here.

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.IntegerField()
    data_nascimento = models.DateField(max_length=255)
    data_cliente = models.DateField(auto_now_add=True)


