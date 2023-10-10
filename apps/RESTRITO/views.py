from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from CADASTRO.models import CadastroUsuario
from GUIAS.models import GuiaConsulta
from RESTRITO.forms import VerificadorForm, AuditoriaForm

# EM CONSTRUÇÃO ===================================================================================
@login_required
def home(request):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if  not usuario_ativo.is_aprovador  \
  and not usuario_ativo.is_faturador  \
  and not usuario_ativo.is_faturador  \
  and not usuario_ativo.is_auditor    \
  and not usuario_ativo.is_administrador:
    return redirect('/')
  
  context = { 'usuario_ativo': usuario_ativo }

  return render(request, 'restrito/home.html', context)

@login_required
def em_construcao(request):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if  not usuario_ativo.is_aprovador  \
  and not usuario_ativo.is_faturador  \
  and not usuario_ativo.is_faturador  \
  and not usuario_ativo.is_auditor    \
  and not usuario_ativo.is_administrador:
    return redirect('/')
  
  context = { 'usuario_ativo': usuario_ativo }

  return render(request, 'restrito/em_construcao.html', context)


# APROVACAO =======================================================================================
@login_required
def ap_consulta_solicitadas(request):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_aprovador:
    return redirect('/restrito/')
  
  consultas_list = GuiaConsulta.objects.filter(status = 'Aguardando').order_by('criacao_data')

  paginator = Paginator(consultas_list, 10)

  page = request.GET.get('page')

  header = 'Guias de Consulta para Aprovação'

  context = { 
    'consultas': paginator.get_page(page), 
    'usuario_ativo': usuario_ativo,
    'header': header
  }

  return render(request, 'restrito/aprovacao/consulta-lista.html', context)

@login_required
def ap_consulta_canceladas(request):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_aprovador:
    return redirect('/restrito/')
  
  consultas_list = GuiaConsulta.objects.filter(status = 'Cancelada').filter(cancelamento_usuario = request.user).order_by('criacao_data')

  paginator = Paginator(consultas_list, 10)

  page = request.GET.get('page')

  header = 'Guias de Consulta Cancealadas'

  context = { 
    'consultas': paginator.get_page(page), 
    'usuario_ativo': usuario_ativo,
    'header': header
  }

  return render(request, 'restrito/aprovacao/consulta-lista.html', context)

@login_required
def ap_consulta_aprovadas(request):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_aprovador:
    return redirect('/restrito/')
  
  consultas_list = GuiaConsulta.objects.filter(status = 'Aprovada').order_by('criacao_data')

  paginator = Paginator(consultas_list, 10)

  page = request.GET.get('page')

  header = 'Guias de Consulta Aprovadas'

  context = { 
    'consultas': paginator.get_page(page), 
    'usuario_ativo': usuario_ativo,
    'header': header
  }

  return render(request, 'restrito/aprovacao/consulta-lista.html', context)

@login_required
def ap_consulta_detalhe(request, id):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_aprovador:
    return redirect('/restrito/')

  consulta = get_object_or_404(GuiaConsulta, pk=id)
  cadastro = get_object_or_404(CadastroUsuario, login = consulta.criacao_usuario)

  context = {
    'consulta': consulta,
    'cadastro': cadastro,
    'usuario_ativo': usuario_ativo,
  }

  return render(request, 'restrito/aprovacao/consulta-detalhe.html', context)

@login_required
def ap_consulta_aprovar(request, id):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_aprovador:
    return redirect('/restrito/')

  consulta = get_object_or_404(GuiaConsulta, pk=id)

  if consulta.status == 'Aguardando':
    consulta.status = 'Aprovada'
    consulta.aprovacao_usuario = request.user
    consulta.aprovacao_data = datetime.now()
    consulta.save()
    # return redirect('restrito:ap-consulta-aprovadas')
    return redirect('/restrito/ap/consulta-detalhe/{}'.format(id))
    
  
  if consulta.status == 'Cancelada':
    consulta.status = 'Aprovada'
    consulta.aprovacao_usuario = request.user
    consulta.aprovacao_data = datetime.now()
    consulta.cancelamento_usuario = None
    consulta.cancelamento_data = None
    consulta.save()
    return redirect('/restrito/ap/consulta-detalhe/{}'.format(id))
    
  return redirect('restrito:ap-consulta-solicitadas')

@login_required
def ap_consulta_cancelar(request, id):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_aprovador:
    return redirect('/restrito/')

  consulta = get_object_or_404(GuiaConsulta, pk=id)

  if consulta.status == 'Aguardando' or consulta.status == 'Aprovada':
    consulta.status = 'Cancelada'
    consulta.cancelamento_usuario = request.user
    consulta.cancelamento_data = datetime.now()
    consulta.save()
    return redirect('/restrito/ap/consulta-detalhe/{}'.format(id))

  
  return redirect('restrito:ap-consulta-solicitadas')


# FATURAMENTO =====================================================================================
@login_required
def fa_consulta_aprovadas(request):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_faturador:
    return redirect('/restrito/')
  
  consultas_list = GuiaConsulta.objects \
    .filter(credenciado = usuario_ativo.credenciado_acesso) \
    .filter(status = 'Aprovada') \
    .order_by('criacao_data')

  paginator = Paginator(consultas_list, 10)

  page = request.GET.get('page')

  header = 'Guias de Consulta Aguardando Faturamento'

  context = { 
    'consultas': paginator.get_page(page), 
    'usuario_ativo': usuario_ativo,
    'header': header
  }

  return render(request, 'restrito/faturamento/consulta-lista.html', context)

@login_required
def fa_consulta_faturadas(request):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_faturador:
    return redirect('/restrito/')
  
  consultas_list = GuiaConsulta.objects \
    .filter(credenciado = usuario_ativo.credenciado_acesso) \
    .filter(status = 'Faturada') \
    .order_by('criacao_data')

  paginator = Paginator(consultas_list, 10)

  page = request.GET.get('page')

  header = 'Guias de Consulta Faturadas'

  context = { 
    'consultas': paginator.get_page(page), 
    'usuario_ativo': usuario_ativo,
    'header': header
  }

  return render(request, 'restrito/faturamento/consulta-lista.html', context)

@login_required
def fa_consulta_detalhe(request, id):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_faturador:
    return redirect('/restrito/')

  consulta = get_object_or_404(GuiaConsulta, pk=id)
  cadastro = get_object_or_404(CadastroUsuario, login = consulta.criacao_usuario)

  context = {
    'consulta': consulta,
    'cadastro': cadastro,
    'usuario_ativo': usuario_ativo,
    'msg': '',
  }

  if request.method == 'POST':
    context['form'] = VerificadorForm(request.POST)

    if context['form'].is_valid():
      if context['form'].data['verificador'] == consulta.verificador:
        context['consulta'].status = 'Faturada'
        context['consulta'].faturamento_usuario = request.user
        context['consulta'].faturamento_data = datetime.now()
        context['consulta'].save()
        # return redirect('/restrito/fa/consulta-faturadas/')
      
        context['msg'] = 'Guia faturada com sucesso!'
        return render(request, 'restrito/faturamento/consulta-detalhe.html', context)  

      else:
        context['form'] = VerificadorForm()
        context['msg'] = 'Código verificador incorreto!'
        return render(request, 'restrito/faturamento/consulta-detalhe.html', context)  
    else:
      context['form'] = VerificadorForm()
      return render(request, 'restrito/faturamento/consulta-detalhe.html', context)
  else:
    context['form'] = VerificadorForm()
    return render(request, 'restrito/faturamento/consulta-detalhe.html', context)
  


# AUDITORIA =======================================================================================
@login_required
def au_consulta_faturadas(request):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_auditor:
    return redirect('/restrito/')

  consultas_list = GuiaConsulta.objects \
    .filter(status = 'Faturada') \
    .order_by('criacao_data')

  paginator = Paginator(consultas_list, 10)

  page = request.GET.get('page')

  header = 'Guias de Consulta Aguardando Auditoria'

  context = { 
    'consultas': paginator.get_page(page), 
    'usuario_ativo': usuario_ativo,
    'header': header
  }

  return render(request, 'restrito/auditoria/consulta-lista.html', context)

@login_required
def au_consulta_auditadas(request):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_auditor:
    return redirect('/restrito/')

  consultas_list = GuiaConsulta.objects \
    .filter(status = 'Auditada') \
    .order_by('criacao_data')

  paginator = Paginator(consultas_list, 10)

  page = request.GET.get('page')

  header = 'Guias de Consulta Aguardando Auditoria'

  context = { 
    'consultas': paginator.get_page(page), 
    'usuario_ativo': usuario_ativo,
    'header': header
  }

  return render(request, 'restrito/auditoria/consulta-lista.html', context)

@login_required
def au_consulta_detalhe(request, id):
  usuario_ativo = get_object_or_404(CadastroUsuario, login = request.user)

  if not usuario_ativo.is_auditor:
    return redirect('/restrito/')

  consulta = get_object_or_404(GuiaConsulta, pk=id)
  cadastro = get_object_or_404(CadastroUsuario, login = consulta.criacao_usuario)

  context = {
    'consulta': consulta,
    'cadastro': cadastro,
    'usuario_ativo': usuario_ativo,
    'msg': '',
  }

  if request.method == 'POST':
    context['form'] = AuditoriaForm(request.POST)
    if context['form'].is_valid():       
      context['consulta'].status = 'Auditada'
      context['consulta'].coparticipacao = context['form'].data['valor']
      context['consulta'].auditoria_usuario = request.user
      context['consulta'].auditoria_data = datetime.now()
      context['consulta'].save()
      context['msg'] = 'Guia auditada com sucesso!'
      return render(request, 'restrito/auditoria/consulta-detalhe.html', context)  
    else:
      context['form'] = AuditoriaForm()
      return render(request, 'restrito/auditoria/consulta-detalhe.html', context)
  else:
    context['form'] = AuditoriaForm()
    return render(request, 'restrito/auditoria/consulta-detalhe.html', context)
  