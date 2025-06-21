function abrirModalCuidado() {
  const form = document.querySelector("#modalCuidado form");
  form.reset();
  form.action = agregarCuidadoURL;

  const plantaSelect = document.getElementById("planta_id_display");
  plantaSelect.disabled = false;
  plantaSelect.selectedIndex = 0;

  document.getElementById("planta_id_real").value = plantaSelect.value;

  document.querySelectorAll('#formCuidado select, #formCuidado input, #formCuidado textarea').forEach(el => el.disabled = false);
  document.querySelector('#formCuidado button[type="submit"]').classList.remove('hidden');

  document.getElementById("modalCuidado").classList.remove("hidden");
}

function cerrarModalCuidado() {
  document.getElementById("modalCuidado").classList.add("hidden");
}

function editarCuidado(id, plantaId, tipo, dias, fecha, hora, detalles) {
  const form = document.querySelector('#modalCuidado form');
  form.action = `/cuidados/editar/${id}/`;

  const plantaSelect = document.getElementById("planta_id_display");
  plantaSelect.value = plantaId;
  plantaSelect.disabled = true;

  document.getElementById("planta_id_real").value = plantaId;
  document.querySelector('[name="tipo_cuidado"]').value = tipo;
  document.querySelector('[name="frecuen_dias"]').value = dias;
  document.querySelector('[name="prox_fecha"]').value = fecha;
  document.querySelector('[name="hora"]').value = hora;
  document.querySelector('[name="detalles"]').value = detalles;

  document.getElementById("modalCuidado").classList.remove("hidden");
}

function verCuidado(planta, tipo, dias, fecha, hora, detalles) {
  document.getElementById("verPlanta").textContent = planta;
  document.getElementById("verTipo").textContent = tipo;
  document.getElementById("verFrecuencia").textContent = dias;
  document.getElementById("verFecha").textContent = fecha;
  document.getElementById("verHora").textContent = hora || "-";
  document.getElementById("verDetalles").textContent = detalles || "-";

  document.getElementById("modalVerCuidado").classList.remove("hidden");
}

function cerrarModalVerCuidado() {
  document.getElementById("modalVerCuidado").classList.add("hidden");
}


document.addEventListener("DOMContentLoaded", () => {
  const plantaSelect = document.getElementById("planta_id_display");
  if (plantaSelect) {
    plantaSelect.addEventListener("change", function () {
      document.getElementById("planta_id_real").value = this.value;
    });
  }
});
