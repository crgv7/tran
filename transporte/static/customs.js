
function pantalla() {
    console.log("se ejecuta la funcion")
    var element=document.getElementById("contenedor")
    var element2=document.getElementById("principal")
    if (screen.width<600) {
        element.removeAttribute("class")
        element.setAttribute("class","container-sm mt-4 rounded-3 shadow border-dark colorprincipal")

        element2.removeAttribute("class")
        element2.setAttribute("class","row container-sm d-inline-block")

        
    }
}

pantalla()