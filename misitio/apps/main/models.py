from django.db import models
from django.contrib.auth.models import User
import os
import uuid

def url_upload_candidatos(self, filename):	
		f, ext = os.path.splitext(filename)	
		ruta = "app/candidatos/%s%s" % (uuid.uuid4().hex, ext)
		return ruta

class Candidato(models.Model):
	nombre = models.CharField(max_length=144, blank=True, null=True)
	apellido = models.CharField(max_length=144, blank=True, null=True)
	foto = models.ImageField(upload_to=url_upload_candidatos, blank=True, null=True)

	def __unicode__(self):
		return "%s %s" % (self.nombre, self.apellido)

class VotosManager(models.Manager):
	def crear_voto(self, candidato, usuario, voto):
		us = User.objects.get(username=usuario)
		voto = self.create(candidato_id=candidato, user=us, voto=1)
		return voto


class Votos(models.Model):
	candidato = models.ForeignKey(Candidato, related_name="votos_candidatos")
	user = models.OneToOneField(User, related_name="votos_usuario")
	voto = models.IntegerField(blank=True, null=True)

	def votos(self):
		return self.voto > 0
	votos.boolean = True

	def __unicode__(self):
		return "%s" % self.voto

	objects = VotosManager()
