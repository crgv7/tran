var pasaje=false
var cargas=false

function pasajes(cargas){
    
    if(cargas==true){
      console.log("entre al if")
      document.getElementById("carga").remove();
      document.getElementById("lbcarga").remove();
    }

    var element=document.getElementById("id_cantidad_km").cloneNode(true)
    var element2=document.createElement("label")
    element2.setAttribute("id","lbpasajero")
    element2.innerText="Pasajeros"
    
    element.setAttribute("id","pasajeros")
    element.setAttribute("name", "cantidad_pasajeros")


    var padre=document.getElementById("opcion")
    padre.appendChild(element2)
    padre.appendChild(element)
    pasaje=true
    cargas=false
  


//document.getElementById("pasajeros").removeAttribute('class');
  //document.getElementById("pasajeros").setAttribute('class', 'mb-3');
}

function carga(pasaje){
  if(pasaje==true){
    console.log("entre al if")
    document.getElementById("pasajeros").remove();
    document.getElementById("lbpasajero").remove();
  }
  var element=document.getElementById("id_cantidad_km").cloneNode(true)
  var element2=document.createElement("label")
  element2.innerText="Peso"
  element2.setAttribute("id","lbcarga")

  element.setAttribute("id", "carga")
  element.setAttribute("name", "cantidad_peso")




  var padre=document.getElementById("opcion")
  padre.appendChild(element2)
  padre.appendChild(element)
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
