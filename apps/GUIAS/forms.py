from django import forms

from GUIAS.models import GuiaConsulta
from CADASTRO.models import Credenciado, Especialidade

# class GuiaConsultaForm(forms.ModelForm):

#   class Meta:
#     model =  GuiaConsulta
#     # fields = ['especialidade', 'credenciado']
#     fields = ['especialidade',]





class GuiaConsultaForm(forms.Form):
  especialidade = forms.ModelChoiceField(
    queryset=Especialidade.objects.all().order_by('nome'), 
    label='Especialidade',
  )

  credenciado = forms.ModelChoiceField(
    queryset=Credenciado.objects.all().order_by('nome'),
    label='Credenciado',
  )
  