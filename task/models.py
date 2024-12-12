from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from stdimage.models import StdImageField
from django.db import models

class Tarefa(models.Model):
   titulo = models.CharField(max_length=100, unique=True)
   concluida = models.BooleanField(default=False)
   usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   imagem = StdImageField(upload_to='tarefas', variations={'thumb': (100, 100)}, blank=True, null=True)

   def __str__(self):
       return self.titulo

   class Meta:
       ordering = ['-id']

   def clean(self):
       if Tarefa.objects.filter(titulo=self.titulo, usuario=self.usuario).exclude(id=self.id).exists():
           raise ValidationError('Você já possui uma tarefa com este título.')