const formulario=document.getElementById( 'aut');
const inputs=document.querySelectorAll('#aut input ');
const pass=document.getElementById('passs')
const correo=document.getElementById('correo')




formulario.addEventListener('submit',(e) => { 
    e.preventDefault();
    const st = correo.value.includes('@');
     
    if(pass.value.length !=0 && correo.value.length !=0 && st)   {
         window.location.href = "panel/";  
        
    }});
