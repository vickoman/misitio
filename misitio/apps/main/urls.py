from django.conf.urls import patterns, include, url

urlpatterns = patterns('misitio.apps.main.views',
		url(r'^$', 'index_view', name="url_home"),
		url(r'^ajax/votar/$', 'VotarAjaxView', name="url_votar_ajax"),
		url(r'^ajax/voto/deshacer', 'DeshacerVoto', name="url_deshacer_voto"),
		url(r'^logout', 'logout', name="url_logout"),

	)