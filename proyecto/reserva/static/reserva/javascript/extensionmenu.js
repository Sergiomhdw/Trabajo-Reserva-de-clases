var titulo = document.getElementById("Perfil-menu-oculto2"); //Creacion de la extension de mis reservas
var a = document.createElement("a");
a.innerHTML = "Mis reservas";
a.setAttribute('href', "/reserva/misreservas/")
titulo.appendChild(a);