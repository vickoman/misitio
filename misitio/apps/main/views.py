from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from models import *
from django.contrib.auth import logout as auth_logout
from django.db.models import Count
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
import json


def index_view(request):	
	candidatos = Candidato.objects.all()
	mivoto = Votos.objects.filter(user__username=request.user)		
	template = "main/index.html"	
	ctx = {"candidatos" : candidatos, "mivoto" : mivoto}
	return render_to_response(template,ctx, context_instance=RequestContext(request))

def VotarAjaxView(request):	
	if request.is_ajax():
		#votos = Votos.objects.filter(candidato = request.POST['id_candidato'])		
		votos = Votos.objects.filter(user__id=request.user.pk)
		if votos:
			mensaje = "Ya"
		else:
			voto = Votos.objects.crear_voto(request.POST['id_candidato'], request.user.username, 1)
			if voto:
				mensaje = "OK"
			else:
				mensaje = "NO"
	else:
		raise Http404
	response_data = {}
	response_data['mensaje'] = mensaje
	response_data['id'] = request.POST['id_candidato']
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def DeshacerVoto(request):
	if request.is_ajax():
		voto = Votos.objects.filter(candidato__id=request.POST['id_candidato'], user__id=request.user.pk)
		if voto:	
			voto.delete()		
			mensaje = "OK"
		else:
			mensaje = "NO"
	else:
		raise Http404
	response_data = {}
	response_data['mensaje'] = mensaje
	response_data['id_candidato'] = request.POST['id_candidato']
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def logout(request):    
    auth_logout(request)
    return HttpResponseRedirect('/')


