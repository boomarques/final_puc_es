from django.urls import path
from GUIAS import views

app_name = 'guias'

urlpatterns = [
  path('', views.home, name='home'),

  path('consulta-lista/', views.consulta_lista, name='consulta-lista'),
  
  path('consulta-detalhe/<int:id>', views.consulta_detalhe, name='consulta-detalhe'),

  path('consulta-nova/', views.consulta_nova, name='consulta-nova'),

  path('consulta-cancelamento/<int:id>', views.consulta_cancelamento, name='consulta-cancelamento'),
    
  
  #------------------------------------------------------------------------------------------------
  
  path('exame-novo/', views.em_construcao, name='exame-novo'),

  path('exame-lista/', views.em_construcao, name='exame-lista'),

  path('financeiro/', views.em_construcao, name='financeiro'),

  path('credenciados/', views.credenciados, name='credenciados'),


]
