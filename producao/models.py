# coding: utf8

from django.db import models

class Fornecedor(models.Model):

	razao_social = models.CharField(max_length=120, verbose_name="Razão Social", null=True, blank=True)
	fantasia = models.CharField(max_length=120, verbose_name="Fantasia")
	cnpj_cpf = models.CharField(max_length=16, verbose_name="CPF/CNPJ", null=True, blank=True)
	endereco = models.CharField(max_length=200, verbose_name="Endereço", null=True, blank=True)
	numero = models.CharField(max_length=6, verbose_name="Núm.", null=True, blank=True)
	complemento = models.CharField(max_length=16, verbose_name="Compl.", null=True, blank=True)
	cep = models.CharField(max_length=8, verbose_name="CEP", null=True, blank=True)
	bairro = models.CharField(max_length=80, verbose_name="Bairro", null=True, blank=True)
	cidade = models.CharField(max_length=80, verbose_name="Cidade", null=True, blank=True)
	estado = models.CharField(max_length=2, verbose_name="Estado", null=True, blank=True)
	pais = models.CharField(max_length=32, verbose_name="País", null=True, blank=True)
	observacao = models.CharField(max_length=255, verbose_name="Observação", null=True, blank=True)
	site = models.CharField(max_length=120, null=True, blank=True)
	observacao = models.TextField(verbose_name="observação", blank=True, null=True)

	def __unicode__(self):
		return self.fantasia


	class Meta:
		verbose_name_plural = "fornecedores"
			
#============================================================================================#

class Cliente(models.Model):
	
	razao_social = models.CharField(max_length=120, verbose_name="Razão Social", null=True, blank=True)
	fantasia = models.CharField(max_length=120, verbose_name="Fantasia")
	cnpj_cpf = models.CharField(max_length=16, verbose_name="CPF/CNPJ", null=True, blank=True)
	endereco = models.CharField(max_length=200, verbose_name="Endereço", null=True, blank=True)
	numero = models.CharField(max_length=6, verbose_name="Núm.", null=True, blank=True)
	complemento = models.CharField(max_length=16, verbose_name="Compl.", null=True, blank=True)
	cep = models.CharField(max_length=8, verbose_name="CEP", null=True, blank=True)
	bairro = models.CharField(max_length=80, verbose_name="Bairro", null=True, blank=True)
	cidade = models.CharField(max_length=80, verbose_name="Cidade", null=True, blank=True)
	estado = models.CharField(max_length=2, verbose_name="Estado", null=True, blank=True)
	pais = models.CharField(max_length=32, verbose_name="País", null=True, blank=True)
	observacao = models.CharField(max_length=255, verbose_name="Observação", null=True, blank=True)
	site = models.CharField(max_length=120, null=True, blank=True)
	observacao = models.TextField(verbose_name="observação", blank=True, null=True)

	def __unicode__(self):
		return self.fantasia

#============================================================================================#

class Transportadora(models.Model):
	
	razao_social = models.CharField(max_length=120, verbose_name="Razão Social", null=True, blank=True)
	fantasia = models.CharField(max_length=120, verbose_name="Fantasia")
	cnpj_cpf = models.CharField(max_length=16, verbose_name="CPF/CNPJ", null=True, blank=True)
	endereco = models.CharField(max_length=200, verbose_name="Endereço", null=True, blank=True)
	numero = models.CharField(max_length=6, verbose_name="Núm.", null=True, blank=True)
	complemento = models.CharField(max_length=16, verbose_name="Compl.", null=True, blank=True)
	cep = models.CharField(max_length=8, verbose_name="CEP", null=True, blank=True)
	bairro = models.CharField(max_length=80, verbose_name="Bairro", null=True, blank=True)
	cidade = models.CharField(max_length=80, verbose_name="Cidade", null=True, blank=True)
	estado = models.CharField(max_length=2, verbose_name="Estado", null=True, blank=True)
	pais = models.CharField(max_length=32, verbose_name="País", null=True, blank=True)
	observacao = models.CharField(max_length=255, verbose_name="Observação", null=True, blank=True)
	site = models.CharField(max_length=120, null=True, blank=True)
	observacao = models.TextField(verbose_name="observação", blank=True, null=True)
	
	def __unicode__(self):
		return self.fantasia

#============================================================================================#

class ContatoEmFornecedor(models.Model):
	
	fornecedor = models.ForeignKey(Fornecedor)
	nome = models.CharField(max_length=120)
	telefone1 = models.CharField(max_length=20, verbose_name='telefone 1', blank=True, null=True)
	telefone2 = models.CharField(max_length=20, verbose_name='telefone 2', blank=True, null=True)
	email1 = models.CharField(max_length=100, verbose_name='email 1', blank=True, null=True)
	email2 = models.CharField(max_length=100, verbose_name='email 2', blank=True, null=True)

	def __unicode__(self):
		return str(self.fornecedor)
	
	class Meta:
		verbose_name_plural = "contato em fornecedores"

#============================================================================================#

class ContatoEmCliente(models.Model):
	
	cliente = models.ForeignKey(Cliente)
	nome = models.CharField(max_length=120)
	telefone1 = models.CharField(max_length=20, verbose_name='telefone 1', blank=True, null=True)
	telefone2 = models.CharField(max_length=20, verbose_name='telefone 2', blank=True, null=True)
	email1 = models.CharField(max_length=100, verbose_name='email 1', blank=True, null=True)
	email2 = models.CharField(max_length=100, verbose_name='email 2', blank=True, null=True)

	def __unicode__(self):
		return self.contato.nome

#============================================================================================#

class ContatoEmTransportadora(models.Model):
	
	transportadora = models.ForeignKey(Transportadora)
	nome = models.CharField(max_length=120)
	telefone1 = models.CharField(max_length=20, verbose_name='telefone 1', blank=True, null=True)
	telefone2 = models.CharField(max_length=20, verbose_name='telefone 2', blank=True, null=True)
	email1 = models.CharField(max_length=100, verbose_name='email 1', blank=True, null=True)
	email2 = models.CharField(max_length=100, verbose_name='email 2', blank=True, null=True)

	def __unicode__(self):
		return self.contato.nome

#============================================================================================#

class BancoEmFornecedor(models.Model):
	
	fornecedor = models.ForeignKey(Fornecedor)
	cedente = models.CharField(max_length=120, blank=True, null=True)
	banco = models.CharField(max_length=60, blank=True, null=True)	
	agencia = models.CharField(max_length=12, verbose_name="agência", blank=True, null=True)
	cc = models.CharField(max_length=12, verbose_name="conta corrente", blank=True, null=True)
	operacao = models.CharField(max_length=12, verbose_name="operação", blank=True, null=True)
	
	def __unicode__(self):
		return self.banco
	
	class Meta:
		verbose_name_plural = "banco em fornecedores"

#============================================================================================#

class Fabricante(models.Model):

	nome = models.CharField(max_length=120)
	site = models.CharField(max_length=120, blank=True, null=True)
	observacao = models.TextField(verbose_name="observação", blank=True, null=True)

	def __unicode__(self):
		return self.nome

#============================================================================================#

class Funcionario(models.Model):
	
	primeiro_nome = models.CharField(max_length=16, unique=True)
	sobrenome = models.CharField(max_length=60, null=True)
	simbolo = models.ImageField(upload_to="funcionario/", verbose_name="símbolo")
	observacao = models.TextField(verbose_name="observação", blank=True, null=True)

	def __unicode__(self):
		return self.primeiro_nome

	class Meta:
		verbose_name = "funcionário"

#============================================================================================#

class GrupoComponente(models.Model):
	
	nome = models.CharField(max_length=120)
	prefixo = models.CharField(max_length=10)
	
	def __unicode__(self):
		return self.nome
	
	class Meta:
		verbose_name = "grupo de componentes"
		verbose_name_plural = "grupos de componentes"	


#============================================================================================#

class UltimoPartNumber(models.Model):
	
	grupo = models.ForeignKey(GrupoComponente, unique=True)
	part_number = models.CharField(max_length=4, verbose_name="Part-Number")

	def __unicode__(self):
		return str(self.grupo.prefixo) + str(self.part_number)


#============================================================================================#

class Componente(models.Model):
	
	ORIGEM = (
		('1', 'Nacional'),
		('2', 'Importado'),
	)
	
	UNIDADE = (
		('1', 'Unidades'),
		('2', 'Metros'),
		('3', 'Centímetros'),
		('4', 'Milímetros'),
	)

	grupo = models.ForeignKey(GrupoComponente)
	mestria_pn = models.CharField(max_length=20, verbose_name="Mestria Part-Number", blank=True)
	fabricante = models.ForeignKey(Fabricante, null=True)
	fabricante_pn = models.CharField(max_length=24, verbose_name="Fabricante Part-Number", null=True)
	fornecedor = models.ForeignKey(Fornecedor, null=True)
	fornecedor_pn = models.CharField(max_length=24, verbose_name="Fornecedor Part-Number", null=True)
	origem = models.CharField(max_length=1, choices=ORIGEM)
	descricao = models.CharField(max_length=120, verbose_name="Descrição")
	lead_time = models.IntegerField(verbose_name="Lead Time", blank=True, null=True)
	preco_medio = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Preço Médio (R$)", blank=True, null=True)
	unidade = models.CharField(max_length=1, choices=UNIDADE)
	est_reserva = models.PositiveIntegerField(verbose_name="Estoque de Reserva")
	est_producao = models.PositiveIntegerField(verbose_name="Estoque de Produção")
	ncm = models.CharField(verbose_name="NCM", max_length=20, blank=True, null=True)

	def mestria_part_number(self):
		return self.mestria_pn
	mestria_part_number.short_description = "Mestria Part-Number"

	def save(self):
		if not self.mestria_pn:
			ultimo_pn = UltimoPartNumber.objects.filter(grupo=self.grupo)
			if ultimo_pn:
				ultimo_pn = UltimoPartNumber.objects.get(grupo=self.grupo)
				aux = int(ultimo_pn.part_number) + 1
				aux = str(aux)
				zeros = 4 - len(aux)
				for i in range(zeros): #@UnusedVariable
					aux = "0" + aux
				self.mestria_pn = str(self.grupo.prefixo) + aux
				ultimo_pn.part_number = aux
				ultimo_pn.save()
			else:
				self.mestria_pn = str(self.grupo.prefixo) + "0001"
				ultimo_pn = UltimoPartNumber(grupo=self.grupo, part_number="0001")
				ultimo_pn.save()

		super(Componente, self).save()


	def __unicode__(self):
		return self.mestria_pn


#============================================================================================#

class Produto(models.Model):
	
	nome = models.CharField(max_length=120)
	arquivo1 = models.FileField(upload_to="produtos/", blank=True, null=True, verbose_name="arquivo 1")
	arquivo2 = models.FileField(upload_to="produtos/", blank=True, null=True, verbose_name="arquivo 2")
	arquivo3 = models.FileField(upload_to="produtos/", blank=True, null=True, verbose_name="arquivo 3")
	est_reserva = models.PositiveIntegerField(verbose_name="Estoque Reserva", default=0)
	est_producao = models.PositiveIntegerField(verbose_name="Estoque Produção", default=0)
	qnt_montado = models.PositiveIntegerField(verbose_name="Quantidade Montado", default=0)
	qnt_testando = models.PositiveIntegerField(verbose_name="Quantidade em Teste", default=0)
	qnt_testado = models.PositiveIntegerField(verbose_name="Quantidade Testado", default=0)
	qnt_na_caixa = models.PositiveIntegerField(verbose_name="Quantidade na Caixa", default=0)

	def __unicode__(self):
		return self.nome
	
#============================================================================================#

class ComponenteEmProduto(models.Model):

	produto = models.ForeignKey(Produto)
	componente = models.ForeignKey(Componente)
	tag = models.CharField(max_length=10)
	quantidade = models.PositiveIntegerField()


	def __unicode__(self):
		return str(self.componente) + "/" + str(self.produto)


	class Meta:
		verbose_name = "Componentes do Produto"
		verbose_name_plural = "Componentes do Produto"


#============================================================================================#

class ProdutoEmProduto(models.Model):

	produto_pai = models.ForeignKey(Produto, related_name="produto_pai")
	sub_produto = models.ForeignKey(Produto, related_name="sub_produto", verbose_name="subproduto")
	quantidade = models.PositiveIntegerField()

	class Meta:
		verbose_name = "subproduto"

#============================================================================================#

class Pedido(models.Model):
	
	STATUS = (
		('1', 'Em aberto'),
		('2', 'Recebido'),
		('3', 'Cancelado'),
	)
	
	fornecedor = models.ForeignKey(Fornecedor, blank=True, null=True)
	data_abertura = models.DateField(verbose_name="data de abertura")
	data_fechamento = models.DateField(verbose_name="data de fechamento", blank=True, null=True)
	observacao = models.TextField(verbose_name="observação")
	transportadora = models.ForeignKey(Transportadora, blank=True, null=True)
	valor_transportadora = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
	valor_outros_gastos = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
	descricao_outros_gastos = models.CharField(max_length=255, blank=True, null=True)
	status = models.CharField(max_length=1, choices=STATUS, default='1')

	def __unicode__(self):
		return str(self.fornecedor)


#============================================================================================#

class ComponenteEmPedido(models.Model):

	STATUS = (
		('1', 'Em aberto'),
		('2', 'Recebido'),
	)	

	pedido = models.ForeignKey(Pedido)
	componente = models.ForeignKey(Componente)
	quantidade = models.PositiveIntegerField()
	valor = models.DecimalField(max_digits=7, decimal_places=2)
	total = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
	status = models.CharField(max_length=1, choices=STATUS, default='1')

	def save(self):
		self.total = self.quantidade * self.valor
		super(ComponenteEmPedido, self).save()

	def __unicode__(self):
		return str(self.componente) + "/" + str(self.pedido)
	
#============================================================================================#

class DefeitoComponente(models.Model):
	
	tipo = models.CharField(max_length=60)
	sigla = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.tipo
	
	class Meta:
		verbose_name = "defeito em componente"
		verbose_name_plural = "defeitos em componente"

#============================================================================================#

class ProdutoMontado(models.Model):
	
	produto = models.ForeignKey(Produto)
	quantidade = models.PositiveIntegerField()
	funcionario = models.ForeignKey(Funcionario, verbose_name="funcionário")
	data = models.DateField()
	observacao = models.TextField(verbose_name="observação", blank=True, null=True)
	
	def __unicode__(self):
		return str(self.produto)

	class Meta:
		verbose_name_plural = "produtos montados"