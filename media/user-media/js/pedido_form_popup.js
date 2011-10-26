var popupStatus = 0;

function loadPopup() {
	if(popupStatus == 0) {
		$("#form_popup").fadeIn("fast");
		popupStatus = 1;
	}
}

function disablePopup() {
	if(popupStatus == 1) {
		$("#form_popup").fadeOut("fast");
		popupStatus = 0;
	}
}

function centerPopup() {
	var windowWidth = document.documentElement.clientWidth;
	var windowHeight = document.documentElement.clientHeight;
	var popupWidth = $("#form_popup").width();
	var popupHeight = $("#form_popup").height();
	
	$("#form_popup").css ({
		"position": "absolute",
		"top": windowHeight/2-popupHeight/2,
		"left": windowWidth/2-popupWidth/2
	});
}

$(document).ready(function() {
		
	$(".row_link").click(function(){
		$("#form_popup h3").html($("#nome_componente", this).html());
		$("#quantidade").attr('value', "");
		$("#valor").attr('value', "");
		$("#comp_id").attr('value', $("#id_componente", this).html());
		
		$("#submit").attr('class', "btn primary");	// Aparece botao salvar 
		$("#submit2").attr('class', "hidden");		// Esconde outro botao
		
		// Esconde botoes Excluir e Receber
		$("#exclui_comp").attr('class', "hidden");
		$("#recebe_comp").attr('class', "hidden");
		
		centerPopup();
		loadPopup();
	});
	
	$(".row_link_cp").click(function(){
		$("#form_popup h3").html($("#nome_componente", this).html());
		$("#quantidade").attr('value', $("#cp_qntd", this).html());
		var valor = $("#cp_valor", this).html().replace("R$ ", "");
		$("#valor").attr('value', valor);
		$("#comp_id").attr('value', $("#cp_id", this).html());
		
		$("#submit2").attr('class', "btn primary");	// Aparece botao salvar
		$("#submit").attr('class', "hidden"); 		// Esconde outro botao
		
		// Mostra botoes Excluir e Receber
		$("#exclui_comp").attr('class', "btn danger");
		$("#recebe_comp").attr('class', "btn success");

		centerPopup();
		loadPopup();
	});
	
	$("#form_popup_close").click(function() {
		disablePopup();
	});
	
	$(document).keypress(function(e){
		if(e.keyCode==27 && popupStatus==1){
			disablePopup();
		}
	});
	
	$("#submit").click(function(){	
		var quantidade_val = $("#quantidade").val();
		var valor_val = $("#valor").val();
		var pedido_id_val = $("#pedido_id").val();
		var comp_id_val = $("#comp_id").val();
		
		/* Tratamento de dados */
		valor_val = valor_val.replace(",", ".");
		
		$.post("/pedidos/insere-componente-pedido/", {
			quantidade: quantidade_val,
			valor: valor_val,
			pedido_id: pedido_id_val,
			comp_id: comp_id_val
		}, function(data) {
			location.reload();
		});
	});
	
	$("#submit2").click(function(){
		var quantidade_val = $("#quantidade").val();
		var valor_val = $("#valor").val();
		var pedido_id_val = $("#pedido_id").val();
		var comp_id_val = $("#comp_id").val();
		
		/* Tratamento de dados */
		valor_val = valor_val.replace(",", ".");
		
		$.post("/pedidos/edita-componente-pedido/", {
			quantidade: quantidade_val,
			valor: valor_val,
			pedido_id: pedido_id_val,
			comp_id: comp_id_val
		}, function(data) {
			location.reload();
		});
	});
	
	$("#exclui_comp").click(function() {
		if(confirm("Excluir componente do pedido?")) {
			var cp_id_val = $("#comp_id").val();
			var pedido_id_val = $("#pedido_id").val();
			
			$.post("/pedidos/exclui-componente-pedido/", {
				pedido_id: pedido_id_val,
				cp_id: cp_id_val
			}, function(data) {
				location.reload();
			});	
		}
	});
	
});























