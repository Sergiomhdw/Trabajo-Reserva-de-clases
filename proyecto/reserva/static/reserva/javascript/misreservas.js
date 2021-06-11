
let staff = document.getElementById("staff");
let profesor = "";
if (staff.innerHTML == "True"){
    profesor = "";
}
else{
    profesor = staff.className;
    console.log(profesor)
}
let info = document.getElementById("informacion");
    while (info.firstChild) {
        info.removeChild(info.firstChild);
    }


$.ajax({
    url: "/reserva/detallemisreservas_inicio",
    method: "GET",
    dataType:"json",
    data:{
        'profesor':profesor,
    },
    success:function(datos){
        console.log("success");
        console.log(datos);
        if(datos.reservas==" "){
            document.getElementById("error").style.display="block";
            document.getElementById("contador").innerHTML="<p>Reservas activas: 0 </p>";

        }else{
            reservas=JSON.parse(datos.reservas);
            clases=JSON.parse(datos.clases);
            profesores=JSON.parse(datos.profesores);
            
            creacionreserva(reservas,profesores,clases);
        }
        
    },
    error:function(datos){
        console.log("Error controlado por el servidor");
        
    }  
    });

function cambio(){

    let info = document.getElementById("informacion");
    while (info.firstChild) {
        info.removeChild(info.firstChild);
    }
    document.getElementById("error").style.display="none";
    let fecha = document.getElementById("fecha").value;
    let evento = document.getElementById("evento").value;


    $.ajax({
        url: "/reserva/detallemisreservas",
        method: "GET",
        dataType:"json",
        data:{
            'fecha':fecha,
            'evento':evento,
            'profesor':profesor,

        },

        success:function(datos){
            console.log("success");
        if(datos.reservas==" "){
            document.getElementById("error").style.display="block";
            document.getElementById("contador").innerHTML="<p>Reservas activas: 0 </p>";
        }else{
            reservas=JSON.parse(datos.reservas);
            clases=JSON.parse(datos.clases);
            profesores=JSON.parse(datos.profesores);
            
            creacionreserva(reservas,profesores,clases);
        }
        },
        error:function(datos){
            console.log("Error controlado por el servidor");
            
        }  
        });

}

function creacionreserva(reservas,profesores,clases){

    let info = document.getElementById("informacion");
    while (info.firstChild) {
        info.removeChild(info.firstChild);
    }
    
    let contador=0;
        reservas.forEach(reserva => {

            let dictprofe= new Map();
                for(let profesor of profesores){
                    dictprofe.set(profesor.pk, profesor.fields.name +" "+ profesor.fields.lastname);
                                   
                }
            let dictclase= new Map();
                for(let clase of clases){
                    dictclase.set(clase.pk, clase.fields.name);
                                   
                }

            let horainicio=reserva.fields.horainicio.split("T")[1].split(":");
            let hora1=horainicio[0]+":"+horainicio[1]
            let horafinal=reserva.fields.horafinal.split("T")[1].split(":");
            let hora2=horafinal[0]+":"+horafinal[1]

            contador++;
            let dia =  document.createElement("div");
            dia.className="dia";
            let datos = document.createElement("div");
            datos.className="datos";

            let p1 = document.createElement("p");
            p1.textContent = "Fecha: "+reserva.fields.reservationday +" de "+ hora1 + " a " + hora2;

            let boton1 = document.createElement("button");
            boton1.innerHTML = "<lord-icon src='https://cdn.lordicon.com/gsqxdxog.json' trigger='morph-two-way' colors='primary:#ffffff,secondary:#ffffff' stroke='100' style='width:40px;height:40px'></lord-icon>";
            boton1.id = reserva.pk;
            boton1.onclick=function(){
                borrar(reserva.pk);
            }


            dia.appendChild(p1);
            dia.appendChild(boton1);

            if(staff.innerHTML=="True"){
                let h3 = document.createElement("h3");
                h3.textContent = " Profesor: "+ dictprofe.get(reserva.fields.profesor);
                datos.appendChild(h3);
                // FALTAN COSAS EL NOMBRE DEL PROF CON EL DICCIONARION UN ROLLO
            }

            let p5 =document.createElement("p");
            p5.textContent = " Clase: "+ dictclase.get(reserva.fields.clase);

            

            let p2 = document.createElement("p");
            p2.textContent = "Curso: "+ reserva.fields.curso;

            let p3 = document.createElement("p");
            p3.textContent = "Motivo: "+reserva.fields.motivo;

            let p4 = document.createElement("p");
            p4.textContent = "Alumnos: "+reserva.fields.cantidad;

            datos.appendChild(p5);
            datos.appendChild(p2);
            datos.appendChild(p3);
            datos.appendChild(p4);

            
            info.appendChild(dia);
            info.appendChild(datos);

         

        });
        document.getElementById("contador").innerHTML="<p>Reservas activas: "+contador+"</p>";
}
function borrar(idreserva){
    if (window.confirm("¿Estas seguro que quieres borrar la reserva?")) {
        $.ajax({
            url: "/reserva/eliminarreserva",
            method: "GET",
            dataType:"json",
            data:{
                'idreserva':idreserva
            },
            success:function(datos){
                location.reload();
               
            },
            error:function(datos){
                console.log("Error controlado por el servidor");
                
            }  
            });
      }
}
