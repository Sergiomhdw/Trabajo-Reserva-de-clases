from django.contrib import admin
from reserva.models import Clase, Reserv

# Register your models here.

class ClaseAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ReservAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Clase, ClaseAdmin)
admin.site.register(Reserv, ReservAdmin)