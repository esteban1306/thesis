#Importar objeto para renderizar la solicitud o mostrar error 404 en la pagina
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
#Importar objetos http para el procesamiento de solicitudes, y redireccionar a otras paginas
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#Importar modelos necesarios para construir las vistas
from models import Tipodocente, Docentes, Caracter, Evaluacionestrabajogrado
#Importar los modelos de formularios creados en forms.py
from forms import LoginForm, TipodocenteForm, DocentesForm, CaracterForm, EvaluacionesTrabajoGradoForm
#Importar objetos de autenticacion de django
from django.contrib.auth import login, logout, authenticate

# Creacion de vistas

#Definicion de vista principal 
def home(request):
	#Formulario de login
	loginForm = LoginForm()
	#Si la solicitud fue enviada...
	if request.method == 'POST':
		#El formulario es enlazado mediante este metodo 
		loginForm = LoginForm(request.POST)
		#Verificar si el formulario cumple con las condiciones de validacion
        if loginForm.is_valid():
        	#Limpiar datos ingresados...
            username  = loginForm.cleaned_data['username']
            password  = loginForm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                #Redireccionar despues del envio de datos
                return HttpResponseRedirect('/')
  	loginForm = LoginForm()
  	#Envio final del formulario
	ctx = {'loginForm':loginForm}
	return render_to_response('home.html', ctx, context_instance=RequestContext(request))

#Definicion de vista para el login	
def login_view(request):
	mensaje = ""
	#Si el usuario se ha autenticado
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		#Si la solicitud fue enviada...
		if request.method == "POST":
			form = LoginForm(request.POST)
			#Verificar si el formulario cumple con las condiciones de validacion
			if form.is_valid():
				#Limpia los datos ingresados de nombre de usuario y contrasena
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				#Procede a autenticar el usuario
				usuario = authenticate(username=username,password=password)
				#Verificar si el usuario existe y si esta activo
				if usuario is not None and usuario.is_active:
					#Enviar la peticion web con el usuario autenticado
					login(request, usuario)
					return HttpResponseRedirect('/')
				#Si no se autentica el usuario
				else:
					#Mostrar un mensaje indicando los fallos
					mensaje = "usuario y/o password incorrecto"
		form = LoginForm()
		#Envio final del formulario con datos
		ctx = {'form':form, 'mensaje':mensaje}
		#Redirecciona a la pagina del login
		return render_to_response('login.html', ctx, context_instance=RequestContext(request))

#Definicion de vista para cierre de sesion
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

#Definicion de vista para lista de estudiantes
def lista_estudiantes(request):
	tiposDocentes = Tipodocente.objects.all()
	return render_to_response('lista_estudiantes.html',{'lista':tiposDocentes})

#Definicion de vista para formulario de prueba
def pruebaForm(request):
	#Crear un formulario para el tipo de docente
	formulario = TipodocenteForm()
	ctx = {'form':formulario}
	return render_to_response('registrarTipoDocente.html', ctx, context_instance=RequestContext(request))

#Definicion de vista para el tipo de docente
def nuevo_Tipodocente(request):

	#Si la solicitud fue enviada...
	if request.method=='POST':
		formulario = TipodocenteForm(request.POST or None, request.FILES)
		#Verificar si el formulario cumple con las condiciones de validacion
		if formulario.is_valid():
			#Almacena el formulario con sus datos
			formulario.save()
			return HttpResponseRedirect('/Tipodocente')
	else:
		formulario = Tipodocente()
	return render_to_response('registrarTipoDocente.html',{'formulario':formulario}, context_instance=RequestContext(request))

#Definicion de vista para un nuevo docente
def nuevo_Docente(request):
	Tipodocente_id=Tipodocente.objects.all()

	#Si la solicitud fue enviada...
	if request.method=='POST':
		formulario = DocentesForm(request.POST, request.FILES)
		#Verificar si el formulario cumple con las condiciones de validacion
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/Docentes')
	else:
		formulario = Docentes()
	return render_to_response('registrarDocente.html',{'formulario':formulario}, context_instance=RequestContext(request))

#Definicion de vista para un nuevo caracter
def nuevo_Caracter(request):

	#Si la solicitud fue enviada...
	if request.method=='POST':
		#Crea el formulario con los datos de la solicitud
		formulario = CaracterForm(request.POST, request.FILES)
		#Verificar si el formulario cumple con las condiciones de validacion
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/Caracter')
	else:
		formulario = Caracter()
	return render_to_response('registrarCaracter.html', {'formulario':formulario}, context_instance=RequestContext(request))

#Definicion de vista para una nueva evaluacion de un trabajo de grado
def nuevo_EvaluacionesTrabajoGrado(request):
	caracter=Caracter.objects.all()
	if request.method=='POST':
		formulario = DocentesForm(request.POST, request.FILES)
		#Verificar si el formulario cumple con las condiciones de validacion
		if formulario.is_valid():
			#Almacena el formulario y redirecciona a la pagina docentes
			formulario.save()
			return HttpResponseRedirect('/Docentes')
	else:
		formulario = Docentes()
	return render_to_response('registrarDocente.html',{'formulario':formulario}, context_instance=RequestContext(request))