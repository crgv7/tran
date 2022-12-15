function pasajes(){
  document.getElementById("kilo").removeAttribute('class');
  document.getElementById("kilo").setAttribute('class', 'mb-3');
  document.getElementById("pasajeros").removeAttribute('class');
  document.getElementById("pasajeros").setAttribute('class', 'mb-3');
}

function carga(){
  document.getElementById("kilo").removeAttribute('class');
  document.getElementById("kilo").setAttribute('class', 'mb-3');
  document.getElementById("peso").removeAttribute('class');
  document.getElementById("peso").setAttribute('class', 'mb-3');
}

function principal(){

  const select = document.getElementsByTagName('select')[0];

  select.addEventListener('change', (event) => {
    //console.log(event.target.value)
      if (event.target.value=="pasaje"){
        pasajes();
      }else if (event.target.value=="carga") {
        carga();

      }
      //resultado.textContent = `Te gusta el sabor ${event.target.value}`;
  });








//ocument.getElementsByTagName("option")[2].onclick=pasajes
//document.getElementById("parrafo").onclick=pasajes;


}

window.onload=principal;
