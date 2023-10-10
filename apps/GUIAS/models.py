from django.db import models
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
 
STATUS = (
  ('Aguardando','Aguardando'),
  ('Aprovada','Aprovada'),
  ('Faturada','Faturada'),
  ('Auditada','Auditada'),
  ('Cancelada','Cancelada'),
)

class GuiaConsulta(models.Model):

  criacao_usuario = models.ForeignKey(
    User,
    on_delete=models.PROTECT, 
    verbose_name='usuário', 
    related_name='criador'
  )

  criacao_data = models.DateTimeField(
    auto_now_add=True
  )

  status = models.CharField(
    max_length=20, 
    choices=STATUS, 
    default=STATUS[0][0],
  )
  
  especialidade = models.CharField(
    max_length=100,
  )
  
  credenciado = models.CharField(
    max_length=100,
  )

  verificador = models.CharField(
    max_length=6, 
    default='000000',
  )
  
  coparticipacao = models.DecimalField(
    decimal_places=2,
    max_digits=10,
    blank=True, 
    null=True,
  )

  aprovacao_usuario = models.ForeignKey(
    User,
    on_delete=models.PROTECT,
    related_name='aprovador',
    blank=True,
    null=True,
  )
  
  aprovacao_data = models.DateTimeField(
    blank=True,
    null=True,
  )

  faturamento_usuario = models.ForeignKey(
    User,
    on_delete=models.PROTECT,
    related_name='faturador',
    blank=True,
    null=True,
    )
  
  faturamento_data = models.DateTimeField(
    blank=True,
    null=True,
  )

  auditoria_usuario = models.ForeignKey(
    User,
    on_delete=models.PROTECT,
    related_name='auditor',
    blank=True,
    null=True,
  )
  
  auditoria_data = models.DateTimeField(
    blank=True,
    null=True,
  )

  cancelamento_usuario = models.ForeignKey(
    User,
    on_delete=models.PROTECT, 
    related_name='cancelador',
    blank=True,
    null=True,
  )
  
  cancelamento_data = models.DateTimeField(
    blank=True,
    null=True,  
  )

  def __str__(self):
    return '{} - {}'.format(self.id, self.criacao_usuario)
