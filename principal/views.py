from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import Tipodocente, Docentes, Caracter, Evaluacionestrabajogrado
from forms import TipodocenteForm, DocentesForm, CaracterForm, EvaluacionesTrabajoGradoForm


# Create your views here.
def lista_estudiantes(request):
	tiposDocentes = Tipodocente.objects.all()
	return render_to_response('lista_estudiantes.html',{'lista':tiposDocentes})

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