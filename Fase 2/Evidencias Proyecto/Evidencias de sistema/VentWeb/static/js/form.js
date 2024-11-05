const formulario = document.querySelector('#formulario')

const procesarTodo = (event) => {
    event.preventDefault();

const dato = new FormData(event.target);

const datosCompletos = Object.fromEntries(datos.entries());
console.log(JSON.stringify(datosCompletos));

}

formulario.addEventListener('submit', procesarTodo);