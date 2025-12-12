from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Rascunho'),
        ('published', 'Publicado'),
    )

    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo