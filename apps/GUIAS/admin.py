from django.contrib import admin

from GUIAS.models import GuiaConsulta 

class GuiaConsultaAdm(admin.ModelAdmin):
  list_display = ('id', 'criacao_usuario', 'especialidade', 'status', 'criacao_data')

admin.site.register(GuiaConsulta, GuiaConsultaAdm)