from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from django.template import Template, Context
from django.contrib.auth.decorators import login_required
from reserva.models import *
from django.core.serializers import serialize
from app.models import Profesor
from datetime import datetime
from .forms import Reserva
from django.urls import reverse
from datetime import date
from django.http import HttpResponseRedirect


@login_required
def aulas(request):
    clases=Clase.objects.all()
    return render(request, "reserva/aulas.html", {"clases":clases})

@login_required
def un_aula(request,id):
    print(request)
    formularioreserva=Reserva()
    clases = get_object_or_404(Clase.objects.filter(id=id))
    clases = Clase.objects.filter(id=id)
    clase=clases[0]
    total_alumnos = clase.capacity
    msgerror="El formulario no es correcto"
    msgok="Se ha creado su reserva"
    if request.method =="POST":
        reserva_form = Reserva(data=request.POST)
        try:
            horai = request.POST['horainicio']
            horaf = request.POST['horafinal']
            dia_act = request.POST.get('fdia','').split("-")
            ahno = int(dia_act[0])
            mes = int(dia_act[1])
            dia = int(dia_act[2])
            dia_actual_cambiado = date(year=ahno, month=mes, day=dia)
            misalumnos = int(request.POST.get('alumnos',''))
            print(horai)
        except:
            return render(request, "reserva/un_aula.html",{"clase":clase,"formulario":formularioreserva,"msg":msgerror})
        if total_alumnos < misalumnos:
            return render(request, "reserva/un_aula.html",{"clase":clase,"formulario":formularioreserva,"msg":msgerror})
        if date.today() > dia_actual_cambiado:
            return render(request, "reserva/un_aula.html",{"clase":clase,"formulario":formularioreserva,"msg":msgerror})
        if horai>=horaf:
            return render(request, "reserva/un_aula.html",{"clase":clase,"formulario":formularioreserva,"msg":msgerror})
        else:

            if reserva_form.is_valid():
                idprofesor = request.user.profesor
                idclase = clase.id
                fdia=request.POST.get('fdia','')
                
                horai = fdia +" "+ request.POST.get('horainicio','')
                horaf = fdia +" "+ request.POST.get('horafinal','')
                descripcion = request.POST.get('descripcion','')
                alumnos = request.POST.get('alumnos','')
                cursos = request.POST.get('cursos','')

                print(idprofesor.id, idclase, fdia, horai, horaf, descripcion, alumnos, cursos)
                Reserv.objects.create(reservationday=fdia,horainicio=horai,horafinal=horaf,cantidad=alumnos,curso=cursos,motivo=descripcion,created=date.today(),updated=date.today(),clase=clase,profesor=idprofesor)
                formularioreserva=Reserva()
                return HttpResponseRedirect(request.path,{"msg":msgok})

    return render(request, "reserva/un_aula.html",{"clase":clase,"formulario":formularioreserva})
    
@login_required
def detallesreserva(request): #obtengo la fecha y la clase y si existereservas le paso los datos al ajax
    print(request)
    id_aula=request.GET["clase"]
    fecha=request.GET["fecha"]
    
    dat = Reserv.objects.filter(clase_id=id_aula).filter(reservationday=fecha)
    if dat.count() > 0 :
        datos={
                'reservas':serialize('json', dat),
                'profesores':serialize('json',Profesor.objects.all()),
                'clases':serialize('json',Clase.objects.all()), 
            }   
    else:
        datos = {
            'reservas': " "
        }
    return JsonResponse(datos)

@login_required
def misreservas(request):
    
    return render(request, "reserva/misreservas.html")
     
@login_required
def detallemisreservas(request):
    profesor=request.GET["profesor"]
    fecha=request.GET["fecha"]
    evento=request.GET["evento"]

    request.user.profesor

    if profesor == "":
        if fecha ==  "" or fecha == "0001-01-01":
            fecha = "vacio"
        if fecha == "vacio" and evento == "":
            dat = Reserv.objects.filter(reservationday__gte=datetime.now())
        elif fecha == "vacio":
            dat = Reserv.objects.filter(motivo=evento).filter(reservationday__gte=datetime.now())

        elif evento == "": 
            dat = Reserv.objects.filter(reservationday=fecha)
        else: 
            dat = Reserv.objects.filter(motivo=evento).filter(reservationday=fecha)
    else:
        if fecha ==  "" or fecha == "0001-01-01":
            fecha = "vacio"
        if fecha == "vacio" and evento == "":
            dat = Reserv.objects.filter(reservationday__gte=datetime.now()).filter(profesor_id=profesor)
        elif fecha == "vacio":
            dat = Reserv.objects.filter(motivo=evento).filter(reservationday__gte=datetime.now()).filter(profesor_id=profesor)

        elif evento == "": 
            dat = Reserv.objects.filter(reservationday=fecha).filter(profesor_id=profesor)
        else: 
            dat = Reserv.objects.filter(motivo=evento).filter(reservationday=fecha).filter(profesor_id=profesor)
        
    if dat.count() > 0 :
        datos={
                'reservas':serialize('json', dat),
                'profesores':serialize('json',Profesor.objects.all()),
                'clases':serialize('json',Clase.objects.all()),
            }
        print(datos)
    else:
        datos = {
            'reservas': " "
        }

    return JsonResponse(datos)

@login_required
def detallemisreservas_inicio(request):
    profesor=request.user.profesor.id
    
    if request.user.is_superuser:
            dat = Reserv.objects.filter(reservationday__gte=datetime.now())
    else:
            profesor = int(profesor)
            dat = Reserv.objects.filter(reservationday__gte=datetime.now()).filter(profesor_id=profesor)
    if dat.count() > 0 :
        datos={
                'reservas':serialize('json', dat),
                'profesores':serialize('json',Profesor.objects.all()),
                'clases':serialize('json',Clase.objects.all()),
            }
    else:
        datos = {
            'reservas': " "
        }
    return JsonResponse(datos)
    


@login_required
def eliminarreserva(request):
    idreserva=request.GET["idreserva"]
    print(idreserva)
    Reserv.objects.filter(id=idreserva).delete()
    datos={
            "msg":"Correcto!"
        }

    return JsonResponse(datos)

    