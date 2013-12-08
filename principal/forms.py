#encoding:utf-8
from django.forms import ModelForm
from django import forms
from models import Tipodocente, Docentes, Caracter, Evaluacionestrabajogrado

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'ingrese su usuario'}))
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))	

class TipodocenteForm(ModelForm):
	class Meta:
		model = Tipodocente
			
class DocentesForm(ModelForm):
	class Meta:
		model = Docentes	

class CaracterForm(ModelForm):
	class Meta:
		model = Caracter

class EvaluacionesTrabajoGradoForm(ModelForm):
	class Meta:
		model = Evaluacionestrabajogrado	