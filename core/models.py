from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    comentarios = models.ManyToManyField(Comentario)
    atracoes = models.ManyToManyField(Atracao)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='pontos_turisticos', null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Pontos Turisticos'


    def __str__(self):
        return self.nome
        