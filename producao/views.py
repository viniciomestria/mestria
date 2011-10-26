# -*- coding: utf-8 -*- 

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, InvalidPage, EmptyPage

import unicodedata
from aux import str_to_money, converte_data

from models import *
from forms import *

#============================================================================#

def home(request):
	return render_to_response('producao/home.html')

#============================================================================#

def pedidos(request):
	lista_pedidos = list(Pedido.objects.all().order_by('-data_abertura'))
	
	for l in lista_pedidos:
		if l.status == '1':
			l.status = "Em aberto"
		elif l.status == '2':
			l.status = "Recebido"
		elif l.status == '3':
			l.status = "Cancelado"
	
	paginator = Paginator(lista_pedidos, 30)

	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	
	try:
		pedidos = paginator.page(page)
	except (EmptyPage, InvalidPage):
		pedidos = paginator.page(paginator.num_pages)
	
	return render_to_response('producao/pedidos/pedidos.html', {
		"pedidos": pedidos,
	})

#============================================================================#

@csrf_exempt
def novo_pedido(request):
	if request.method == "POST":
		form = PedidoRestritoForm(request.POST)
		if form.is_valid():
			p = form.save()
			return redirect('/pedidos/' + str(p.pk))
	else:
		form = PedidoRestritoForm()
	return render_to_response('producao/pedidos/novo_pedido.html', {
		"form": form,
	})

#============================================================================#

@csrf_exempt
def ver_pedido(request, id_pedido):
	pp = get_object_or_404(Pedido, pk=id_pedido)

	if pp.status != '1':
		cancelado = True
	else:
		cancelado = False

	mensagem = ""
	if request.method == 'POST':
		fornecedor_id = int(request.POST['fornecedor'])
		pp.fornecedor = Fornecedor.objects.get(pk=fornecedor_id)
		pp.data_abertura = converte_data(request.POST['data_abertura'])
		pp.observacao = request.POST['observacao']
		pp.save()
		mensagem = "Pedido salvo com sucesso!"
		
	form = PedidoRestritoForm(instance=pp)
	return render_to_response('producao/pedidos/ver_pedido.html', {
		"pedido": pp,
		"form": form,
		"mensagem": mensagem,
		"cancelado": cancelado,
	})

#============================================================================#

@csrf_exempt
def componente_em_pedido(request, id_pedido):
	pedido = get_object_or_404(Pedido, pk=id_pedido)
	componentes_do_fornecedor = list(Componente.objects.filter(fornecedor=pedido.fornecedor))[:500]
	componentes_do_pedido = list(ComponenteEmPedido.objects.filter(pedido=id_pedido))[:500]
	total_qnt_componentes = 0
	total_valor_componentes = 0
	
	# Verificando se pedido esta em aberto
	editavel = True
	if pedido.status != '1':
		editavel = False

	for cp in componentes_do_pedido:
		
		total_qnt_componentes += cp.quantidade
		total_valor_componentes += cp.total
		
		# Substituindo . por virgula
		cp.valor = str(cp.valor).replace(".", ",")
		cp.total = str(cp.total).replace(".", ",")
		
		# Consertando digitos apos a virgula
		cp.valor = str_to_money(cp.valor)
		cp.total = str_to_money(cp.total)
		
		#removendo itens que ja estao no pedido
		for cf in componentes_do_fornecedor:
			if cf.id == cp.componente.id:
				componentes_do_fornecedor.remove(cf)
				break
	
	total_valor_componentes = str(total_valor_componentes).replace(".", ",")
	total_valor_componentes = str_to_money(total_valor_componentes)
	
	return render_to_response('producao/pedidos/componente_em_pedido.html', {
		"pedido": pedido,
		"componentes_do_fornecedor": componentes_do_fornecedor,
		"componentes_do_pedido": componentes_do_pedido,
		"total_qnt_componentes": total_qnt_componentes,
		"total_valor_componentes": total_valor_componentes,
		"editavel": editavel,
	})

#============================================================================#

@csrf_exempt
def insere_componente_pedido(request):
	if request.method == 'POST':
		pedido_id_n = request.POST["pedido_id"]
		componente_id_n = request.POST["comp_id"]
		quantidade_n = int(request.POST["quantidade"])
		valor_n = float(request.POST["valor"])
		
		pedido_n = Pedido.objects.get(pk=pedido_id_n)
		componente_n = Componente.objects.get(pk=componente_id_n)
		
		cp = ComponenteEmPedido(pedido=pedido_n, componente=componente_n, quantidade=quantidade_n, valor=valor_n)
		cp.save()
		return redirect('/pedidos/' + pedido_id_n + '/componentes')
	else:
		return render_to_response('producao/erro.html')

#============================================================================#

@csrf_exempt
def edita_componente_pedido(request):
	if request.method == 'POST':
		cp_id = int(request.POST["comp_id"])
		pedido_id_n = request.POST["pedido_id"]
		quantidade_n = int(request.POST["quantidade"])
		valor_n = float(request.POST["valor"])
		
		cp = ComponenteEmPedido.objects.get(pk=cp_id)
		cp.valor = valor_n
		cp.quantidade = quantidade_n
		cp.save()
		return redirect('/pedidos/' + pedido_id_n + '/componentes')
	else:
		return render_to_response('producao/erro.html')

#============================================================================#

@csrf_exempt
def exclui_componente_pedido(request):
	if request.method == 'POST':
		cp_id = int(request.POST["cp_id"])
		pedido_id = request.POST["pedido_id"]
		cp = ComponenteEmPedido.objects.get(pk=cp_id)
		cp.delete()
		return redirect('/pedidos/' + pedido_id + '/componentes')
	else:
		return render_to_response('producao/erro.html')
	
#============================================================================#

@csrf_exempt
def cancela_pedido(request):
	if request.method == 'POST':
		pedido_id = int(request.POST['pedido_id'])
		p = Pedido.objects.get(pk=pedido_id)
		p.status = '3'
		p.save()
		return redirect('/pedidos/')

#============================================================================#

@csrf_exempt
def recebe_pedido(request, id_pedido):
	p = Pedido.objects.get(pk=id_pedido)
	lista_transportadoras = Transportadora.objects.all()
	mensagem = ""

	if request.method == 'POST':
		p.status = '2'

		p.data_fechamento = converte_data(request.POST['data_fechamento'])
		p.observacao = request.POST['observacao']
		trans_id = int(request.POST['transportadora'])
		valor_transportadora = float(request.POST['valor_transportadora'])
		valor_outros_gastos = float(request.POST['valor_outros_gastos'])
		descricao_outros_gastos = request.POST['descricao_outros_gastos']

		trans = get_object_or_404(Transportadora, pk=trans_id)

		p.transportadora = trans;
		p.valor_transportadora = valor_transportadora
		p.valor_outros_gastos = valor_outros_gastos
		p.descricao_outros_gastos = descricao_outros_gastos

		componentes_do_pedido = ComponenteEmPedido.objects.filter(pedido=p)
		for cp in componentes_do_pedido:
			cp.status = '2'
			componente = Componente.objects.get(pk=cp.componente.id)
			componente.est_reserva += cp.quantidade
			componente.save()
			cp.save()
		
		p.save()
		
		return redirect('/pedidos/' + id_pedido)

	return render_to_response('producao/pedidos/receber.html', {
		'pedido': p,
		'mensagem': mensagem,
		'transportadoras': lista_transportadoras,
	})

#============================================================================#

def componentes(request):
	
	# Coletando variaveis do GET
	filtro = {
		'mes_pn': request.GET.get('mes_pn', ''),
		'desc': request.GET.get('desc', ''),
		'orig': request.GET.get('orig', ''),
		'fab': request.GET.get('fab', ''),
		'fab_pn': request.GET.get('fab_pn', ''),
		'forn': request.GET.get('forn', ''),
		'forn_pn': request.GET.get('forn_pn', ''),
	}
	
	# Auxiliar para filtro de origem
	importado = False
	nacional = False
	if filtro['orig'] == '1': nacional = True
	elif filtro['orig'] == '2': importado = True
		
	# Coleta lista com filtros
	lista_componentes = list(Componente.objects.filter(
		mestria_pn__icontains = filtro['mes_pn'],
		descricao__icontains = filtro['desc'],
		origem__icontains = filtro['orig'],
		fabricante__nome__icontains = filtro['fab'],
		fabricante_pn__icontains = filtro['fab_pn'],
		fornecedor__fantasia__icontains = filtro['forn'],
		fornecedor_pn__icontains = filtro['forn_pn'],
	))

	for comp in lista_componentes:
		
		# Consertando unidades
		if comp.unidade == '1': comp.unidade = 'Unid.'
		if comp.unidade == '2': comp.unidade = 'm'
		if comp.unidade == '3': comp.unidade = 'cm'
		if comp.unidade == '4': comp.unidade = 'mm'
		
		# Alterando virgula
		comp.preco_medio = str(comp.preco_medio).replace('.', ',')
		
	paginator = Paginator(lista_componentes, 30)
	
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

	try:
		componentes = paginator.page(page)
	except (EmptyPage, InvalidPage):
		componentes = paginator.page(paginator.num_pages)

	return render_to_response('producao/componentes/componentes.html', {
		'componentes': componentes,
		'filtro': filtro,
		'nacional': nacional,
		'importado': importado,
	})

#============================================================================#

def ver_componente(request, id_componente):

	comp = get_object_or_404(Componente, pk=id_componente)
	
	# Preparando origem
	if comp.origem == '1': comp.origem = 'Nacional'
	else: comp.origem = 'Importado'

	# Preparando unidade
	if comp.unidade == '1': comp.unidade = 'Unidades'
	if comp.unidade == '2': comp.unidade = 'Metros'
	if comp.unidade == '3': comp.unidade = 'Centímetros'
	if comp.unidade == '4': comp.unidade = 'Milímetros'

	# Preparando preco medio
	comp.preco_medio = str(comp.preco_medio).replace('.', ',')
	comp.preco_medio = str_to_money(comp.preco_medio)

	return render_to_response('producao/componentes/ver_componente.html', {
		'comp': comp,
	})

#============================================================================#

@csrf_exempt
def movimenta_componente(request, id_componente):

	comp = get_object_or_404(Componente, pk=id_componente)
	
	if request.method == 'POST':
		caminho = request.POST['caminho']
		quantidade = int(request.POST['quantidade'])

		if caminho == '1':
			comp.est_reserva -= quantidade
			comp.est_producao += quantidade
			comp.save()
		else:
			comp.est_reserva += quantidade
			comp.est_producao -= quantidade
			comp.save()
		
		return redirect('/componentes/' + str(id_componente))

	return render_to_response('producao/componentes/movimenta_componente.html', {
		'comp': comp,
	})

#============================================================================#

def produtos(request):
	
	lista_produtos = Produto.objects.all()
	paginator = Paginator(lista_produtos, 30)

	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1

	try:
		produtos = paginator.page(page)
	except (EmptyPage, InvalidPage):
		produtos = paginator.page(paginator.num_pages)

	return render_to_response('producao/produtos/produtos.html', {
		'produtos': produtos,
	})

#============================================================================#

def ver_produto(request, id_produto):
	
	prod = get_object_or_404(Produto, pk=id_produto)
	subprodutos = ProdutoEmProduto.objects.filter(produto_pai=prod)
	componentes = ComponenteEmProduto.objects.filter(produto=prod)
	return render_to_response('producao/produtos/ver_produto.html', {
		'produto': prod,
		'subprodutos': subprodutos,
		'componentes': componentes,
	})

#============================================================================#

def linha_de_producao(request):
	return render_to_response('producao/linha_de_producao/index.html')

#============================================================================#

def seleciona_produto_montagem(request):
	lista_produtos = Produto.objects.all().order_by('nome')
	return render_to_response('producao/linha_de_producao/seleciona_produto_montagem.html', {
		'lista_produtos': lista_produtos,
	})

#============================================================================#

def montar_produto(request, id_produto):
	prod = get_object_or_404(Produto, pk=id_produto)
	
	if request.method == 'POST':
		pass
	else:
		
		componentes = list(ComponenteEmProduto.objects.filter(produto=prod))
		
		#== Obtendo apenas tags que se repetem
		lista_tags_unicas = []
		lista_todas_tags = []
		tag_atual = ""
		for comp in componentes:
			lista_todas_tags.append(comp.tag)
			if comp.tag != tag_atual:
				lista_tags_unicas.append(comp.tag)
				tag_atual = comp.tag
		for tag in lista_tags_unicas:
			if lista_todas_tags.count(tag) == 1:
				lista_tags_unicas.remove(tag)
		tags_repetidas = lista_tags_unicas
		
		componentes_redundantes = []
		for t in tags_repetidas:
			lista_componentes = ComponenteEmProduto.objects.filter(produto=prod, tag=t)
			componentes_redundantes.append(lista_componentes)
		
		lista_funcionarios = Funcionario.objects.all().order_by('primeiro_nome')
		return render_to_response('producao/linha_de_producao/montar_produto.html', {
			'produto': prod,
			'lista_funcionarios': lista_funcionarios,
			'tags_repetidas': tags_repetidas,
			'componentes_redundantes': componentes_redundantes,
		})
