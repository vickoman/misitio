from models import *
from django.db.models import Count

def topvotciones(request):
	candidatos = Candidato.objects.annotate(num_votos=Count('votos_candidatos')).order_by('-num_votos')
	ctx = {"topcandidatos" : candidatos}
	return ctx

#mi firma
def footertext(request):
	ctx = {"firma" : "Sitio creado por Vickoman tambien conocido por elvicko :D"}
	return ctx