from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import Tipodocente, Docentes, Caracter, Evaluacionestrabajogrado
from forms import LoginForm, TipodocenteForm, DocentesForm, CaracterForm, EvaluacionesTrabajoGradoForm

from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o password incorrecto"
		form = LoginForm()
		ctx = {'form':form, 'mensaje':mensaje}
		return render_to_response('login.html', ctx, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def lista_estudiantes(request):
	tiposDocentes = Tipodocente.objects.all()
	return render_to_response('lista_estudiantes.html',{'lista':tiposDocentes})

def pruebaForm(request):
	formulario = TipodocenteForm()
	ctx = {'form':formulario}
	return render_to_response('registrarTipoDocente.html', ctx, context_instance=RequestContext(request))

def nuevo_Tipodocente(request):
	if request.method=='POST':
		formulario = TipodocenteForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/Tipodocente')
	else:
		formulario = Tipodocente()
	return render_to_response('registrarTipoDocente.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_Docente(request):
	Tipodocente_id=Tipodocente.objects.all()
	if request.method=='POST':
		formulario = DocentesForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/Docentes')
	else:
		formulario = Docentes()
	return render_to_response('registrarDocente.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_Caracter(request):
	if request.method=='POST':
		formulario = CaracterForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/Caracter')
	else:
		formulario = Caracter()
	return render_to_response('registrarCaracter.html', {'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_EvaluacionesTrabajoGrado(request):
	caracter=Caracter.objects.all()
	if request.method=='POST':
		formulario = DocentesForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/Docentes')
	else:
		formulario = Docentes()
	return render_to_response('registrarDocente.html',{'formulario':formulario}, context_instance=RequestContext(request))