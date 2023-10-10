from django.contrib import admin

from CADASTRO.models import Credenciado, CadastroUsuario, Especialidade, Exame


class CredenciadoAdm(admin.ModelAdmin):
  list_display = ('id', 'nome', 'descricao')

class CadastroUsuarioAdm(admin.ModelAdmin):
  list_display = ('id', 'login', 'nome_completo', 'cpf', 'is_cliente', 'is_aprovador', 'is_faturador', 'is_auditor', 'is_administrador')

class EspecialidadeAdm(admin.ModelAdmin):
  list_display = ('id', 'nome')

class ExameAdm(admin.ModelAdmin):
  list_display = ('id', 'nome')

admin.site.register(Credenciado, CredenciadoAdm)
admin.site.register(CadastroUsuario, CadastroUsuarioAdm)
admin.site.register(Especialidade, EspecialidadeAdm)
admin.site.register(Exame, ExameAdm)
