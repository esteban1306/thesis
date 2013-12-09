#encoding:utf-8
from django.forms import ModelForm
from django import forms
from models import Tipodocente, Docentes, Caracter, Evaluacionestrabajogrado

#Crear modelo de formulario para el inicio de sesion
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'ingrese su usuario'}))
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))	

#Crear modelo de formulario para el modelo de clase Tipodocente
class TipodocenteForm(ModelForm):
	class Meta:
		model = Tipodocente

#Crear modelo de formulario para el modelo de clase Docentes			
class DocentesForm(ModelForm):
	class Meta:
		model = Docentes	

#Crear modelo de formulario para el modelo de clase Caracter
class CaracterForm(ModelForm):
	class Meta:
		model = Caracter

#Crear modelo de formulario para el modelo de clase Evaluacioenstrabajogrado
class EvaluacionesTrabajoGradoForm(ModelForm):
	class Meta:
		model = Evaluacionestrabajogrado	