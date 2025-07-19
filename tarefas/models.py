from django.db import models
from django.utils import timezone
from django.urls import reverse


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('tarefa_detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
