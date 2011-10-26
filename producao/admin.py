# -*- coding: utf8 -*-

from mestria.producao.models import *
from django.contrib import admin


class ComponenteAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {
			'fields':(
				'mestria_pn',
				'grupo',
				('fabricante', 'fabricante_pn'),
				('fornecedor', 'fornecedor_pn'),
				'ncm', 'origem', 'descricao', 'lead_time', 'preco_medio', 'unidade', 'est_reserva', 'est_producao',
			),
		})
	]
	readonly_fields = ('mestria_pn', )
	list_display = ('mestria_part_number', 'grupo', 'descricao', 'fabricante', 'fornecedor', 'origem')
	search_fields = ('grupo', 'mestria_pn')
admin.site.register(Componente, ComponenteAdmin)

#=========================================================================================================#

class ContatoEmFornecedorInline(admin.TabularInline):
	model = ContatoEmFornecedor
	extra = 1

#=========================================================================================================#

class ContatoEmClienteInline(admin.TabularInline):
	model = ContatoEmCliente
	extra = 1

#=========================================================================================================#

class ContatoEmTransportadoraInline(admin.TabularInline):
	model = ContatoEmTransportadora
	extra = 2

#=========================================================================================================#

class BancoEmFornecedorInline(admin.TabularInline):
	model = BancoEmFornecedor
	extra = 1

#=========================================================================================================#

class FornecedorAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {
			'fields': ('cnpj_cpf', ('razao_social', 'fantasia'), 'site', 'observacao')
		}),
		('Endereço', {
			'classes': ('collapse',),
			'fields': (('endereco', 'numero', 'complemento'), ('cep', 'bairro'), ('cidade', 'estado', 'pais'))
		}),
	]
	inlines = [ContatoEmFornecedorInline, BancoEmFornecedorInline]

admin.site.register(Fornecedor, FornecedorAdmin)

#=========================================================================================================#

class ClienteAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {
			'fields': ('cnpj_cpf', ('razao_social', 'fantasia'), 'site', 'observacao')
		}),
		('Endereço', {
			'classes': ('collapse',),
			'fields': (('endereco', 'numero', 'complemento'), ('cep', 'bairro'), ('cidade', 'estado', 'pais'))
		}),
	]
	inlines = [ContatoEmClienteInline]

admin.site.register(Cliente, ClienteAdmin)

#=========================================================================================================#

class TransportadoraAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {
			'fields': ('cnpj_cpf', ('razao_social', 'fantasia'), 'site', 'observacao')
		}),
		('Endereço', {
			'classes': ('collapse',),
			'fields': (('endereco', 'numero', 'complemento'), ('cep', 'bairro'), ('cidade', 'estado', 'pais'))
		}),
	]
	inlines = [ContatoEmTransportadoraInline]

admin.site.register(Transportadora, TransportadoraAdmin)

#=========================================================================================================#

class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('primeiro_nome', 'sobrenome', 'simbolo')
admin.site.register(Funcionario, FuncionarioAdmin)

#=========================================================================================================#

class ComponenteEmProdutoInline(admin.TabularInline):
	model = ComponenteEmProduto
	extra = 20

class ProdutoEmProdutoInline(admin.TabularInline):
	model = ProdutoEmProduto
	fk_name = 'produto_pai'
	extra = 3

class ProdutoAdmin(admin.ModelAdmin):
	inlines = [ProdutoEmProdutoInline, ComponenteEmProdutoInline]

admin.site.register(Produto, ProdutoAdmin)

#=========================================================================================================#

admin.site.register(GrupoComponente)
admin.site.register(Fabricante)
admin.site.register(Pedido)
#admin.site.register(ComponenteEmPedido)
admin.site.register(DefeitoComponente)
admin.site.register(ProdutoMontado)

