// static/js/plantas.js

function abrirModal() {
  document.getElementById("modalPlanta").classList.remove("hidden");
}

function cerrarModal() {
  document.getElementById("modalPlanta").classList.add("hidden");
}

function abrirModalEditar(id, nombre, tipo, cuidados) {
  console.log("ID recibido:", id);
  document.getElementById("editar_id").value = id;
  document.getElementById("editar_nombre").value = nombre;
  document.getElementById("editar_tipo").value = tipo;
  document.getElementById("editar_cuidados").value = cuidados;
  document.getElementById("modalEditarPlanta").classList.remove("hidden");
  document.getElementById("formEditar").action = `/editar_planta/${id}/`;
}

function cerrarModalEditar() {
  document.getElementById("modalEditarPlanta").classList.add("hidden");
}

function abrirModalEliminar(id) {
  const form = document.getElementById("formEliminar");
  form.action = `/eliminar_planta/${id}/`;
  document.getElementById("modalEliminar").classList.remove("hidden");
}

function cerrarModalEliminar() {
  document.getElementById("modalEliminar").classList.add("hidden");
}

function abrirModalVer(nombre, tipo, cuidados, imagenUrl) {
  document.getElementById("ver_nombre").innerText = nombre;
  document.getElementById("ver_tipo").innerText = tipo;
  document.getElementById("ver_cuidados").innerText = cuidados;
  const imagen = document.getElementById("ver_imagen");
  imagen.src = imagenUrl || 'https://via.placeholder.com/128?text=Sin+Imagen';
  document.getElementById("modalVerPlanta").classList.remove("hidden");
}

function cerrarModalVer() {
  document.getElementById("modalVerPlanta").classList.add("hidden");
}
