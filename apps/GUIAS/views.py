from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
# from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from random import randint

from GUIAS.forms import GuiaConsultaForm
from GUIAS.models import GuiaConsulta
from CADASTRO.models import CadastroUsuario, Credenciado, Especialidade

# HOME ============================================================================================
@login_required
def home(request):
  cadastro_usuario = get_object_or_404(CadastroUsuario, login = request.user)

  if cadastro_usuario.is_aprovador:
    return redirect('restrito:home')
  
  if cadastro_usuario.is_faturador:
    return redirect('restrito:home')
  
  if cadastro_usuario.is_auditor:
    return redirect('restrito:home')
  
  if cadastro_usuario.is_administrador:
    return redirect('restrito:home')

  if cadastro_usuario.is_cliente:
    return render(request, 'guias/home.html')
  
  return redirect('/accounts/login')


# CONSULTA ========================================================================================
@login_required
def consulta_lista(request):
  cadastro = get_object_or_404(CadastroUsuario, login = request.user)

  if not cadastro.is_cliente:
    return redirect('/')

  consultas_list = GuiaConsulta.objects.filter(criacao_usuario = request.user).order_by('-criacao_data')

  paginator = Paginator(consultas_list, 10)

  page = request.GET.get('page')

  models = { 'consultas': paginator.get_page(page)}

  return render(request, 'guias/consulta-lista.html', models)

@login_required
def consulta_detalhe(request, id):
  cadastro = get_object_or_404(CadastroUsuario, login = request.user)
  consulta = get_object_or_404(GuiaConsulta, pk=id)

  if consulta.criacao_usuario == request.user:
    return render(request, 'guias/consulta-detalhe.html', {'consulta':consulta, 'cadastro':cadastro})
  else:
    return redirect('guias:consulta-lista')

@login_required
def consulta_nova(request):
  cadastro_usuario = get_object_or_404(CadastroUsuario, login = request.user)

  if not cadastro_usuario.is_cliente:
    return redirect('/')

  if request.method == 'POST':
    form = GuiaConsultaForm(request.POST)

    if form.is_valid():
      consulta = GuiaConsulta.objects.create(
        criacao_usuario = request.user,
        especialidade = get_list_or_404(Especialidade, id = form.data['especialidade'],)[0],
        credenciado = get_list_or_404(Credenciado, id = form.data['credenciado'],)[0],
        verificador = str(randint(99999,999999)),
      )
      return redirect('guias:consulta-lista')

  else:
    form = GuiaConsultaForm()
    return render(request, 'guias/consulta-nova.html', {'form':form})
  
@login_required
def consulta_cancelamento(request, id):
  consulta = get_object_or_404(GuiaConsulta, pk=id)

  if consulta.criacao_usuario != request.user:
    return redirect('guias:consulta-lista')
  
  if consulta.status == 'Aguardando' or consulta.status == 'Aprovada':
    consulta.status = 'Cancelada'
    consulta.cancelamento_usuario = request.user
    consulta.cancelamento_data = datetime.now()
    consulta.save()
    return redirect('guias:consulta-lista')
  
  else:
    return redirect('guias:consulta-lista')


# FINANCEIRO ======================================================================================
@login_required
def credenciados(request):
  cadastro = get_object_or_404(CadastroUsuario, login = request.user)

  if not cadastro.is_cliente:
    return redirect('/')

  return render(request, 'guias/credenciados.html')


# PENDENTES =======================================================================================
@login_required
def em_construcao(request):
  cadastro = get_object_or_404(CadastroUsuario, login = request.user)

  if not cadastro.is_cliente:
    return redirect('/')

  return render(request, 'guias/em-construcao.html')
