// Función para mostrar la imagen de perfil subida
function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('fotodeperfil');
        output.src = reader.result;  // Asigna la imagen cargada al elemento img
    };
    reader.readAsDataURL(event.target.files[0]);  // Lee el archivo cargado
}

    document.addEventListener("DOMContentLoaded", function() {
        // Función para mostrar el formulario de link
        document.getElementById("boton-agregar-link").addEventListener("click", function() {
            var formularioLink = document.getElementById("formulario-link");
            if (formularioLink.style.display === "none" || formularioLink.style.display === "") {
                formularioLink.style.display = "block";
            } else {
                formularioLink.style.display = "none";
            }
        });
    });


