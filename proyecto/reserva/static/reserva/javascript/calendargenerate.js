let selectinicioinicial;
let selectfinalinicial;


$(document).ready(function(){
	
let monthNames = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Diciembre'];
let days=['lunes','martes','miercoles','jueves','viernes','sabado','domingo'];


let currentDate = new Date();   //Guardo el dia de hoy
let currentDay = currentDate.getDate(); //guardo dias
let monthNumber = currentDate.getMonth();//mes
let currentYear = currentDate.getFullYear();//año

let dates = document.getElementById('dates'); //identifico el paratado de dias
let month = document.getElementById('month'); //de meses
let year = document.getElementById('year'); // y años

let prevMonthDOM = document.getElementById('prev-month'); //siguiente mes
let nextMonthDOM = document.getElementById('next-month'); // el mes pasado

month.textContent = monthNames[monthNumber]; //Añadir el nombre al mes
year.textContent = currentYear.toString(); //Añadir el año 

prevMonthDOM.addEventListener('click', ()=>lastMonth()); //al hacer click llamo a la funcion que es para pasar al mes siguiente
nextMonthDOM.addEventListener('click', ()=>nextMonth()); //y esta para volver al mes pasado


const writeMonth = (month) => { //Funcion donde escribo todos los dias

    for(let i = startDay(); i>0;i--){ //Identificar en que numero de dia comienza un mes
        dates.innerHTML += ` <div class="calendar__date calendar__item calendar__last-days">
            ${getTotalDays(monthNumber-1)-(i-1)}
        </div>`;
    }
let contador=startDay();

    for(let i=1; i<=getTotalDays(month); i++){  //Aquí es donde creo todos los dias del mes 
	
        if(i===currentDay) {
            // data-date=${currentYear}-${month+1}-${i} genero la fecha año mes y dia
            dates.innerHTML += ` <div class="calendar__date calendar__item calendar__today" id=${i} data-day=${days[contador]} data-date='${currentYear}-${month+1}-${i}' onclick=comprobar(this.id)>${i}</div>`;
		

        }else{ //Cree dos tipos de dias todos los dias normales y el dia en el que estoy se puede utilizar en futuras ampliaciones
            dates.innerHTML += ` <div class="calendar__date calendar__item" id=${i} data-day=${days[contador]} data-date='${currentYear}-${month+1}-${i}' onclick=comprobar(this.id)>${i}</div>`;

        }
			contador++; 
			if(contador==7){ //voy contando los dias para controlar los dos ulitmo (sabado y domingo) para que estos no se puedan utilizar
				contador=0;
			}
    }
}

const getTotalDays = month => { //para obtener todos los dias totales de cada mes si es de 30 o 31 o si es Febrero 28
    if(month === -1) month = 11;

    if (month == 0 || month == 2 || month == 4 || month == 6 || month == 7 || month == 9 || month == 11) {
        return  31;

    } else if (month == 3 || month == 5 || month == 8 || month == 10) {
        return 30;

    } else {

        return isLeap() ? 29:28; //Aquí llamo a la funcion para ver si un año es bisiesto
    }
}

const isLeap = () => {//La funcion para comprobar si un año es bisiesto
    return ((currentYear % 100 !==0) && (currentYear % 4 === 0) || (currentYear % 400 === 0));
}

const startDay = () => { //Funcion para controlar en que dia de la semana empieza
    let start = new Date(currentYear, monthNumber, 1);
    return ((start.getDay()-1) === -1) ? 6 : start.getDay()-1;
}

const lastMonth = () => { //funcion para todos los meses del año pero hacia atras hasta llegar a 0
    if(monthNumber !== 0){// entonces vuelvo a diciembre y tengo que qquitarle un año al año actua
        monthNumber--;
    }else{
        monthNumber = 11;
        currentYear--;
    }

    setNewDate();//voy llamando a la funcion para que calcule el calendario de ese mes nuevo
}

const nextMonth = () => {   //funcion para ver el mes siguiente voy a ir sumando hasta llegar al tope de nuemeros en el arry
    if(monthNumber !== 11){ //al ser 11 ya que empieza en 0, cuando llegue a 11 que vuelva a empezar en 0
        monthNumber++;
    }else{
        monthNumber = 0;    //al llegar de nuevo a 0 sumo un año mas porque el siguiente de diciembre es enero
        currentYear++;
    }

    setNewDate();//voy llamando a la funcion para que calcule el calendario de ese mes nuevo
}

const setNewDate = () => {  //Cada vez que es llamada calcula el calendario del mes que le pase el año que le pase
    currentDate.setFullYear(currentYear,monthNumber,currentDay); //se le pasa un dia, un mes y un año
    month.textContent = monthNames[monthNumber];//Coge el nombre del mes
    year.textContent = currentYear.toString();//coge el año que se le pasa
    dates.textContent = '';//los dias que se tienen que mostrar
    writeMonth(monthNumber);//LLamo a la funcion que me va a escribir todos los dias que tiene cada mes
}

writeMonth(monthNumber);//Para escribir todos los dias que tiene un mes

})


// let selectfinalinicial=document.getElementById("horafinal");
// console.log(selectinicioinicial);

function comprobar(idelemento){//funcion que comprueba que el dia que yo seleciono no sea ni sabado ni domingo ni que ese dia no pertenezca
    let elemento=document.getElementById(idelemento);
if(elemento.dataset.day=="sabado" || elemento.dataset.day=="domingo" || elemento.dataset==null){
	return;
}else{
    //Aqui muestro la fecha del dia que voy selecionando
    let inputfecha = document.getElementById("fdiamuetra"); 
    let muetrafecha = document.getElementById("fdia");
    inputfecha.setAttribute('value',elemento.dataset.date);
    muetrafecha.setAttribute('value',elemento.dataset.date);

	document.getElementById("formulario").style="";
	document.getElementById("calendar").style="";
    let selecteddate=elemento.dataset.date; //Transformo la fecha para poder trabajar con ella luego
    var path = document.location.pathname; //Cojo la ultima parte de la url que es el id de la clase
    lista = path.split("/");
    id_clase = (lista[3]);

    $.ajax({
        
        url: "/reserva/detallesreserva", //llamo a la url para poder trabajar con la vista en la parte del servidor
        method: "GET",
        dataType:"json",
        data:{
            'clase':id_clase,
            'fecha':selecteddate
        },
        success:function(datos){ //Si la accion se hace exitosamente recibo los datos
                console.log("success");
                let opcionesinicio=document.getElementById("id_horainicio").options; //pongo todas las horas en disponibles
                let opcionesfinal=document.getElementById("id_horafinal").options; //tanto la de las horas de incio como las finales
                for(let option in opcionesinicio){
                    opcionesinicio[option].disabled=false  
                    }
                for(let option in opcionesfinal){
                    opcionesfinal[option].disabled=false  
                    }
            if (datos.reservas == " "){ //si no hay reserva pues muestro un mensaje
                document.getElementById("profere").textContent = "No hay reserva este día";
            }
            else{//si hay reservas tengo que desabilitar las horas escogidas y mostrar las reservas que hay
                reservas = JSON.parse(datos.reservas)
                profesores = JSON.parse(datos.profesores)
    
                let dict= new Map();//Guardo todos los profesores en un diccionario porque trabajo con sus id entonces tengo que mostrar sus nombres
                for(let profesor of profesores){
                    dict.set(profesor.pk, profesor.fields.name +" "+ profesor.fields.lastname);//guardo los profesores con nombre y apellido
                                   
                }

                if(reservas == null){
                    document.getElementById("cursore").textContent = reservas[0].fields.profesor
                }
                
                document.getElementById("profere").textContent = ""; //actualizo los campos antes de recorrer todas las reservas para que no se me acumulen
                for(let reserva of reservas){//recorro todas las reservas para mostrar su informacion

                    let horainicio=reserva.fields.horainicio.split("T")[1].split(":"); //transformo la hora inicial y la hora final
                    let hora1 = reserva.fields.horainicio.split("T")[1]
                    let horafinal=reserva.fields.horafinal.split("T")[1].split(":");
                    let hora2 = reserva.fields.horafinal.split("T")[1]
                    
                    let digito1=parseInt(horainicio[0]);
                    let digito2=parseInt(horafinal[0]);

                    let duracion=digito2-digito1;//calculo si una reserva va a durar varias horas

                    for(let option in opcionesinicio){ //primero voy comprobando en el select de horas iniciales y voy desabilitando para que no puedan elegir
                                                        //una hora si está ocupada
                        if (opcionesinicio[option].value==hora1){
                            opcionesinicio[option].disabled=true;
                            while(duracion>1){
                                duracion--;
                                opcionesinicio[parseInt(option)+duracion].disabled =true;

                            }
                        }
                    }
                    
                    duracion=digito2-digito1;//vuelvo a calcular la duracion porque en el bucle anterior la voy modificando
                    for(let option in opcionesfinal){//hacemos lo mismo que en el bucle de arriba pero para el select de hora final
                        if (opcionesfinal[option].value==hora2){
                            opcionesfinal[option].disabled=true;
                            while(duracion>=1){
                                duracion--;
                                opcionesfinal[parseInt(option)-duracion].disabled =true;
                            }
                        }
                    }

                   
                    var titulo = document.getElementById("profere"); //Una vez que hemos desabilitado las horas que están ocupadas vamos a crear las reservas
                    var motivo = document.getElementById("profere");//para que se vean por pantalla, creo el nombre del profesor, a las hora que está ocupada, y el curso
                    var h3 = document.createElement("h3");
                    var p = document.createElement("p");
                    h3.innerHTML = dict.get(reserva.fields.profesor) + " Con el curso: " + reserva.fields.curso;

                    //A las horas le vulevo a cambiar el formato para que se muestre de una forma simple y facil de entender para el usuario
                    hora1=reserva.fields.horainicio.split("T")[1].split(":");
                    hora1=horainicio[0]+":"+horainicio[1]
                    hora2 = reserva.fields.horafinal.split("T")[1].split(":");
                    hora2=horafinal[0]+":"+horafinal[1]

                    p.innerHTML = reserva.fields.motivo + " de " + hora1 + " a "+ hora2;
                    titulo.appendChild(h3);
                    motivo.appendChild(p);                
                }
            } 
        },
        error:function(datos){//si no hay datos, o ocurre hay algun error que muestre que no hay reservas
            console.log("failure");
            document.getElementById("profere").textContent = "No hay reserva este día";

        }  
        });
    }
}