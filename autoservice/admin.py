from django.contrib import admin
from .models import Automobilo_modelis, Automobilis, Uzsakymas, Uzsakymo_eilute, Paslauga

class UzsakymoEiluteInline(admin.TabularInline):
    model = Uzsakymo_eilute
    extra = 1

class UzsakymasAdmin(admin.ModelAdmin):
    list_display = ('automobilis_id', 'data')
    inlines = [UzsakymoEiluteInline]

class AutomobilisAdmin(admin.ModelAdmin):
    list_display = ('klientas', 'automobilio_modelis_id', 'valstybinis_nr', 'vin_kodas')
    list_filter = ('klientas', 'automobilio_modelis_id')
    search_fields = ('valstybinis_nr', 'vin_kodas')

class PaslaugaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'kaina')

admin.site.register(Automobilo_modelis)
admin.site.register(Automobilis, AutomobilisAdmin)
admin.site.register(Uzsakymas, UzsakymasAdmin)
admin.site.register(Paslauga, PaslaugaAdmin)