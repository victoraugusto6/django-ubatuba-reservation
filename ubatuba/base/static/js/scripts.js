function hide_element_partial_pay() {
    let field_pago = document.getElementById("id_valor_adiantado")
    if (document.getElementById("pago").value == "partial") {
        field_pago.style.display = "block";
    } else {
        field_pago.style.display = "none";
    }
}