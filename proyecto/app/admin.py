from django.contrib import admin
from .models import Profesor
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
# admin.site.register(Profesor)


class ProfesorAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Profesor, ProfesorAdmin)

class EmployeeInline(admin.StackedInline):
    model = Profesor
    can_delete = False
    verbose_name_plural = 'profesors'


