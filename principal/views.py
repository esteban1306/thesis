#Importar objeto para renderizar la solicitud o mostrar error 404 en la pagina
from django.shortcuts import render_to_response, get_object_or_404, render
#Importar objetos http para el procesamiento de solicitudes, y redireccionar a otras paginas
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#Importar modelos necesarios para construir las vistas
from models import *
#Importar los modelos de formularios creados en forms.py
from forms import LoginForm, TipodocenteForm, DocentesForm, CaracterForm, EvaluacionesTrabajoGradoForm
#Importar objetos de autenticacion de django
from django.contrib.auth import login, logout, authenticate

from usuarios.models import Usuario
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template.loader import render_to_string
from django.db.models import Q
from django.db import connection
from django.contrib.auth.models import User
from django.template import Context, Template

# Creacion de vistas

#Definicion de vista principal 
def home(request):
    if request.user.is_authenticated() == False:
        return HttpResponseRedirect('login/')

    ctx = {}
    if request.user.tipo == Usuario.ESTUDIANTE:   # OJO por ahora esto solo funciona con user de tipo ESTUDIANTE 
        ctx['estudiante'] = Estudiantes.objects.get(dni=request.user.dni)
        ctx['perfil']     = ctx['estudiante']

    if request.user.tipo == Usuario.DIRECTOR:
        person = 'Nadie'
    if request.user.tipo == Usuario.COORDINADOR:
        person = 'Nadie'
    if request.user.tipo == Usuario.ASESOR:
        person = 'Nadie'
    if request.user.tipo == Usuario.JURADO:
        person = 'Nadie'


    return render(request, 'home.html', ctx)


def generar_pdf(html):
    # Funcion para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

def estudiante_pdf(request, dni):

    person = Estudiantes.objects.get(dni=dni)
    user = Usuario.objects.get(dni=person.dni)
    asesores_detrabajo = Asesores.objects.filter(Q(trabajosgrado_codigo=person.trabajosgrado_codigo))
    jurados_detrabajo  = Jurados.objects.filter(Q(trabajosgrado_codigo =person.trabajosgrado_codigo))
    ctx = {'person':person, 'usuario':user, 'asesores_detrabajo':asesores_detrabajo, 'jurados_detrabajo':jurados_detrabajo}
    html = render_to_string('estudiante_pdf.html', {'pagesize':'A4', 'person':person,'usuario':user, 'asesores_detrabajo':asesores_detrabajo, 'jurados_detrabajo': jurados_detrabajo}, context_instance=RequestContext(request))
    return generar_pdf(html)

def lista_trabajos_pdf(request):
    trabajos = Trabajosgrado.objects.all()
    html = render_to_string('lista_trabajos_pdf.html',{'pagesize':'A4', 'trabajos':trabajos}, context_instance=RequestContext(request) )
    return generar_pdf(html)

def reporte_criterios_pdf(request):

    rowSet = []
    cursor = connection.cursor()
    cursor.execute("select cj.descripcion as descrip, count(ifo.id)as ctd from (CriteriosJurado cj left join InformeFinal_Criterios ifc on ifc.criteriosjurado_id = cj.id ) left join InformesFinales ifo on ifc.informesfinales_id = ifo.id group by cj.descripcion")
    resultsList = cursor.fetchall()




    for result in resultsList:
        row = []
        for column in result:
           row.append(column)
        rowSet.append(row)
    ctx = {'row':row, 'rowSet':rowSet}
    html = render_to_string('reporte_criterios_pdf.html', {"rowSet":rowSet}, context_instance=RequestContext(request))
    #resultsList = Criteriosjurado.objects.all()
    
    return generar_pdf(html)
    #return render(request, 'reporte_criterios_pdf.html', ctx)

def estudiante_detalle(request, dni):

    estudiante = Estudiantes.objects.get(dni=dni)
    usuario = Usuario.objects.get(dni=estudiante.dni)

    if request.user.tipo == Usuario.ESTUDIANTE:  # OJO por ahora esto solo funciona con user de tipo ESTUDIANTE
        perfil = Estudiantes.objects.get(dni=request.user.dni)

    ctx = {'estudiante':estudiante, 'usuario':usuario, 'perfil':perfil}

    return render(request, 'estudiante_detalle.html', ctx)



def trabajo_grado_detalle(request, codigo):
    trabajo = Trabajosgrado.objects.get(codigo=codigo)
    estudiantes = Estudiantes.objects.filter(trabajosgrado_codigo=trabajo.codigo)

    if request.user.tipo == Usuario.ESTUDIANTE:  # OJO por ahora esto solo funciona con user de tipo ESTUDIANTE
        perfil = Estudiantes.objects.get(dni=request.user.dni)

    ctx = {'trabajo':trabajo, 'estudiantes':estudiantes, 'perfil':perfil}
    return render(request, 'trabajo_grado_detalle.html', ctx)



def trabajos_grado_list(request):
    return render(request, 'trabajos_grado_list.html')
    
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
                    mensaje = "Usuario y/o password incorrecto"
        form = LoginForm()
        #Envio final del formulario con datos
        ctx = {'form':form, 'mensaje':mensaje}
        #Redirecciona a la pagina del login
        return render_to_response('login.html', ctx, context_instance=RequestContext(request))

#Definicion de vista para cierre de sesion
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login')

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

