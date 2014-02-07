from django.contrib import admin
from models import Candidato, Votos

class CandidatoAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'apellido')    
admin.site.register(Candidato, CandidatoAdmin)

class VotosAdmin(admin.ModelAdmin):
	list_display = ('user', 'candidato', 'votos',)
	search_fields = ['candidato__nombre', 'candidato__apellido', 'user__username',]
	list_display_links = ('votos',)
admin.site.register(Votos, VotosAdmin)