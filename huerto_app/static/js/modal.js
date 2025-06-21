// static/js/modal.js

function abrirModal() {
  const modal = document.getElementById("modalPlanta");
  if (modal) modal.classList.remove("hidden");
}

function cerrarModal() {
  const modal = document.getElementById("modalPlanta");
  if (modal) modal.classList.add("hidden");
}
