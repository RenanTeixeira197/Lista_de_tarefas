from django.db import models

class MeuModelo(models.Model):
    # Add your fields here, for example:
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
