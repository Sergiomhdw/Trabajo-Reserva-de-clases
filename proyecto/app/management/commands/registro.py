from django.core.management.base import BaseCommand, CommandError
from app.models import Profesor
from reserva.models import *
import unicodedata
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creacion de profesores'

    def handle(self, *args, **options):
        
        def elimina_tildes(s):
            return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

        manf = open("lista.csv", encoding="utf-8")

        for linea in manf:
            if linea.endswith("\n"):
                linea=linea[1:-2]
            else:
                linea=linea[1:-1]		
            separados = linea.split(",")

            if len(separados)==4:
                nombre=separados[1][1:].replace('"','')
                apellidos=separados[0]
                nick=separados[2].replace('"','')
                print(nick)
                nombre_usuario = separados[1].split(" ")[1].lower()
                apellido_usuario = separados[0].split(" ")[0].lower()
                usuario=f"{elimina_tildes(nombre_usuario)}.{elimina_tildes(apellido_usuario)}"
                print(f"{usuario} -> {nombre} {apellidos}")
                user = User.objects.create_user(nick, separados[3].replace('"',''), "pestillo", first_name=nombre, last_name=apellidos, )
                user.save()
                profesor = Profesor.objects.create(name=nombre_usuario.replace('"',''),lastname=apellido_usuario,user_id=user.id)
                self.stdout.write(self.style.SUCCESS('Successfully closed poll'))                
                profesor.save()


        manf.close()
