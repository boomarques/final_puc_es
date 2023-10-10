from django.urls import include, path
from RESTRITO import views

app_name = 'restrito'

urlpatterns = [
  path('', views.home, name='home'),

  
  # AP - APROVADOR ================================================================================
  
  path('ap/', views.home, name='ap'),

  path('ap/consulta-solicitadas/', views.ap_consulta_solicitadas, name='ap-consulta-solicitadas'),
  path('ap/consulta-aprovadas/', views.ap_consulta_aprovadas, name='ap-consulta-aprovadas'),
  path('ap/consulta-canceladas/', views.ap_consulta_canceladas, name='ap-consulta-canceladas'),
  path('ap/consulta-detalhe/<int:id>', views.ap_consulta_detalhe, name='ap-consulta-detalhe'),
  path('ap/consulta-aprovar/<int:id>', views.ap_consulta_aprovar, name='ap-consulta-aprovar'),
  path('ap/consulta-cancelar/<int:id>', views.ap_consulta_cancelar, name='ap-consulta-cancelar'),

  path('ap/exame-lista/', views.em_construcao, name='ap-exame-lista'),

  
  
  # FA - FATURADOR ================================================================================

  path('fa/', views.home, name='fa'),
  
  path('fa/consulta-aprovadas/', views.fa_consulta_aprovadas, name='fa-consulta-aprovadas'),
  path('fa/consulta-faturadas/', views.fa_consulta_faturadas, name='fa-consulta-faturadas'),
  path('fa/consulta-detalhe/<int:id>', views.fa_consulta_detalhe, name='fa-consulta-detalhe'),

  path('fa/exame-lista/', views.em_construcao, name='fa-exame-lista'),


# AU - AUDITOR ====================================================================================

  path('au/', views.home, name='au'),

  path('au/consulta-faturadas/', views.au_consulta_faturadas, name='au-consulta-faturadas'),
  path('au/consulta-auditadas/', views.au_consulta_auditadas, name='au-consulta-auditadas'),
  path('au/consulta-detalhe/<int:id>', views.au_consulta_detalhe, name='au-consulta-detalhe'),

  path('au/exame-lista/', views.em_construcao, name='au-exame-lista'),

]
