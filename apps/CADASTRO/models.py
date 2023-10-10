from django.db import models
from django.contrib.auth.models import User


class Credenciado(models.Model):
  nome = models.CharField(max_length=100)
  descricao = models.CharField(max_length=255, verbose_name='descrição')

  def __str__(self):
    return '{}'.format(self.nome)
  

class Especialidade(models.Model):
  nome = models.CharField(max_length=100)

  def __str__(self):
    return '{}'.format(self.nome)
  

class Exame(models.Model):
  nome = models.CharField(max_length=100)

  def __str__(self):
    return '{}'.format(self.nome)


class CadastroUsuario(models.Model):
  login = models.OneToOneField(
    User, 
    on_delete=models.PROTECT
  )
  
  nome_completo = models.CharField(
    max_length=100,
    verbose_name='nome completo',
    default='não informado'
  )
  
  cpf = models.CharField(
    max_length=14,
    default='não informado'
  )

  is_cliente = models.BooleanField(default=False)

  is_aprovador = models.BooleanField(default=False)

  is_faturador = models.BooleanField(default=False)

  is_auditor = models.BooleanField(default=False)

  is_administrador = models.BooleanField(default=False)

  credenciado_acesso = models.CharField(
    max_length=100,
    null=True,
    blank=True,
  )

  def __str__(self):
    return '{}: {} - {}'.format(self.login, self.nome_completo, self.cpf)
