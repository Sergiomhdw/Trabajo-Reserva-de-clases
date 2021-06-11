from django import forms
from django.forms.widgets import HiddenInput


class Reserva(forms.Form):
    horas_inicio=[
        ("08:00:00Z","08:00"),
        ("09:00:00Z","09:00"),
        ("10:00:00Z","10:00"),
        ("11:00:00Z","11:00"),
        ("11:30:00Z","11:30"),
        ("12:30:00Z","12:30"),
        ("13:30:00Z","13:30"),
        ("16:00:00Z","16:00"),
        ("17:00:00Z","17:00"),
        ("18:00:00Z","18:00"),
        ("18:30:00Z","18:30"),
        ("19:30:00Z","19:30"),
        ("20:30:00Z","20:30"),
    ]
    
    horas_final=[
        ("09:00:00Z","09:00"),
        ("10:00:00Z","10:00"),
        ("11:00:00Z","11:00"),
        ("11:30:00Z","11:30"),
        ("12:30:00Z","12:30"),
        ("13:30:00Z","13:30"),
        ("14:30:00Z","14:30"),
        ("17:00:00Z","17:00"),
        ("18:00:00Z","18:00"),
        ("18:30:00Z","18:30"),
        ("19:30:00Z","19:30"),
        ("20:30:00Z","20:30"),
        ("21:30:00Z","21:30"),
    ]

    descripcion=[
        ("examen","Examen"),
        ("otro","Otro"),
    ]

    cursos=[
        ("1ESOA","1ESOA"),
        ("2ESOA","2ESOA"),
        ("2ESOB","2ESOb"),
        ("3ESOA","3ESOA"),
        ("3ESOB","3ESOB"),
        ("4ESOA","4ESOA"),
        ("4ESOB","4ESOB"),
        ("1FPB","1FPB"),
        ("2FPB","2FPB"),
        ("otros","Otros"), 
    ]

    
    horainicio=forms.ChoiceField(choices=horas_inicio,required=True,label="Hora de inicio")
    horafinal=forms.ChoiceField(choices=horas_final,required=True,label="Hora final")
    descripcion=forms.ChoiceField(choices=descripcion,required=True,label="Motivo")
    alumnos=forms.IntegerField(required=True,label="Nº Alumnos")
    cursos=forms.ChoiceField(choices=cursos,required=True,label="Curso")
    
