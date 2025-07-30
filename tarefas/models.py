from django.db import models
from django.utils import timezone
from django.urls import reverse

class MeuModelo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('meu_modelo_detail', kwargs={'pk': self.pk})
