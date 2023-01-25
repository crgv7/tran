var pasaje=false
var cargas=false

function pasajes(cargas){
    
    if(cargas==true){
      console.log("entre al if")
      document.getElementById("peso").remove();
    }
    var padre=document.getElementById("opcion")
    var hijo=document.getElementById("pasajeros")
    hijo.removeAttribute('class')
    hijo.setAttribute('class', 'mb-3')
    padre.appendChild(hijo)
    pasaje=true
    cargas=false
  


//document.getElementById("pasajeros").removeAttribute('class');
  //document.getElementById("pasajeros").setAttribute('class', 'mb-3');
}

function carga(pasaje){
  if(pasaje==true){
    console.log("entre al if")
    document.getElementById("pasajeros").remove();
  }
  var padre=document.getElementById("opcion")
  var hijo=document.getElementById("peso")
  hijo.removeAttribute('class')
  hijo.setAttribute('class', 'mb-3')
  padre.appendChild(hijo)
  pasaje=false
  cargas=true
}


function principal(){
  
  const select = document.getElementsByTagName('select')[0]; //selcciona el primer elemnto select del html.

  select.addEventListener('change', (event) => { //añade el evento
    //console.log(event.target.value)
      if (event.target.value=="pasaje"){ // si se selecciona pasaje ejecuta la funcion pasaje()
        pasajes(cargas);
      }else if (event.target.value=="carga") {
        carga(pasaje);

      }
      //resultado.textContent = `Te gusta el sabor ${event.target.value}`;
  });








//ocument.getElementsByTagName("option")[2].onclick=pasajes
//document.getElementById("parrafo").onclick=pasajes;


}

window.onload=principal;
