from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import Tipodocente
from forms import TipodocenteForm

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