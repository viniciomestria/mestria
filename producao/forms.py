from models import *
from django.forms import ModelForm, DateField
from django.forms.widgets import DateTimeInput

DATE_FORMAT = '%d/%m/%Y'

class FormattedDateInput(DateTimeInput):
	format = DATE_FORMAT

class PedidoForm(ModelForm):

	data_abertura = DateField(label="Data de Abertura", input_formats=[DATE_FORMAT])

	class Meta:
		model = Pedido

class PedidoRestritoForm(PedidoForm):
	class Meta(PedidoForm.Meta):
		exclude = (
			'status', 'data_fechamento', 'transportadora', 'valor_transportadora', 'valor_outros_gastos',
			'descricao_outros_gastos')
