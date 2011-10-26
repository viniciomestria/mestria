# -*- coding: utf8 -*-

from django.conf.urls.defaults import *
from django.conf import settings

# Ativando admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	# Administração
	(r'^admin/', include(admin.site.urls)),

	# Media access
	(r'^user-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

	# Home
	(r'^$', 'mestria.producao.views.home'),

	# Pedidos
	(r'^pedidos/$', 'mestria.producao.views.pedidos'),
	(r'^pedidos/novo/$', 'mestria.producao.views.novo_pedido'),
	(r'^pedidos/(?P<id_pedido>\d+)/$', 'mestria.producao.views.ver_pedido'),
	(r'^pedidos/(?P<id_pedido>\d+)/componentes/$', 'mestria.producao.views.componente_em_pedido'),
    (r'^pedidos/insere-componente-pedido/$', 'mestria.producao.views.insere_componente_pedido'),
	(r'^pedidos/edita-componente-pedido/$', 'mestria.producao.views.edita_componente_pedido'),
	(r'^pedidos/exclui-componente-pedido/$', 'mestria.producao.views.exclui_componente_pedido'),
	(r'^pedidos/cancela/$', 'mestria.producao.views.cancela_pedido'),
	(r'^pedidos/(?P<id_pedido>\d+)/receber/$', 'mestria.producao.views.recebe_pedido'),

	# Componentes
	(r'^componentes/$', 'mestria.producao.views.componentes'),
	(r'^componentes/(?P<id_componente>\d+)/$', 'mestria.producao.views.ver_componente'),
	(r'^componentes/(?P<id_componente>\d+)/movimenta/$', 'mestria.producao.views.movimenta_componente'),

	# Produtos
	(r'^produtos/$', 'mestria.producao.views.produtos'),
	(r'^produtos/(?P<id_produto>\d+)/$', 'mestria.producao.views.ver_produto'),
	
	# Linha de producao
	(r'^linha-de-producao/$', 'mestria.producao.views.linha_de_producao'),
	(r'^linha-de-producao/montar-produto/$', 'mestria.producao.views.seleciona_produto_montagem'),
	(r'^linha-de-producao/montar-produto/(?P<id_produto>\d+)/$', 'mestria.producao.views.montar_produto'),

)
