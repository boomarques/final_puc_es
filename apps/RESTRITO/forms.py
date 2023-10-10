from django import forms

class VerificadorForm(forms.Form):
  verificador = forms.IntegerField(
    label='Inserir código de verificação: ',
  )

class AuditoriaForm(forms.Form):
  valor = forms.DecimalField(
    decimal_places=2, 
    max_value=100000, 
    label='Inserir valor de coparticipação: ',
  )