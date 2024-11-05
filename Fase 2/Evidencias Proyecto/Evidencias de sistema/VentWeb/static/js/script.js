let loggedInUser = null; // Variable para almacenar el usuario actualmente conectado
let products = []; // Array para almacenar los productos

// Cargar productos del localStorage al iniciar la página
document.addEventListener("DOMContentLoaded", function () {
    const storedProducts = JSON.parse(localStorage.getItem("products")) || [];
    products = storedProducts;
    displayProducts(products);
});

function togglePublishForm() {
    const form = document.getElementById("publish-form"); // Obtiene el formulario de publicación
    form.style.display = form.style.display === "none" ? "block" : "none"; // Alterna la visibilidad del formulario
}

function openLoginModal() {
    document.getElementById("login-modal").style.display = "block"; // Muestra el modal de inicio de sesión
}

function closeLoginModal() {
    document.getElementById("login-modal").style.display = "none"; // Oculta el modal de inicio de sesión
}

function login() {
    const username = document.getElementById("login-username").value; // Obtiene el nombre de usuario del campo
    if (username) {
        loggedInUser = username; // Almacena el nombre de usuario en la variable
        document.getElementById("username-display").textContent = `Bienvenido, ${username}`; // Muestra un mensaje de bienvenida
        document.getElementById("login-btn").style.display = "none"; // Oculta el botón de inicio de sesión
        document.getElementById("logout-btn").style.display = "inline"; // Muestra el botón de cerrar sesión
        closeLoginModal(); // Cierra el modal de inicio de sesión
    }
}

function logout() {
    loggedInUser = null; // Elimina el usuario conectado
    document.getElementById("username-display").textContent = ""; // Limpia el mensaje de bienvenida
    document.getElementById("login-btn").style.display = "inline"; // Muestra el botón de inicio de sesión
    document.getElementById("logout-btn").style.display = "none"; // Oculta el botón de cerrar sesión
}

function publishProduct() {
    // Verifica si el usuario ha iniciado sesión
    if (!loggedInUser) {
        alert("Debes iniciar sesión para publicar un producto.");
        openLoginModal(); // Abre el modal de inicio de sesión
        return; // Detiene la publicación si no ha iniciado sesión
    }

    const productName = document.getElementById("product-name").value;
    const productDescription = document.getElementById("product-description").value;
    const productPrice = document.getElementById("product-price").value;
    const productLocation = document.getElementById("product-location").value;
    const productCategory = document.getElementById("product-category").value;

    if (productName && productDescription && productPrice && productLocation && productCategory) {
        const newProduct = {
            name: productName,
            description: productDescription,
            price: productPrice,
            location: productLocation,
            category: productCategory,
            image: URL.createObjectURL(document.getElementById("product-images").files[0])
        };

        products.push(newProduct);
        localStorage.setItem("products", JSON.stringify(products)); // Guarda los productos en el localStorage
        displayProducts(products);
        clearForm();
    } else {
        alert("Por favor, completa todos los campos.");
    }
}

function displayProducts(productsToDisplay) {
    const container = document.getElementById("products-container");
    container.innerHTML = ''; // Limpia el contenedor

    productsToDisplay.forEach((product) => {
        const productDiv = document.createElement("div");
        productDiv.classList.add("product");
        productDiv.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p>Precio: $${product.price}</p>
            <p>Ubicación: ${product.location}</p>
            <p>Categoría: ${product.category}</p>
            <button onclick="window.location.href='chat.html'">Chatear aquí</button>
        `;
        container.appendChild(productDiv);
    });
}

function clearForm() {
    document.getElementById("product-name").value = '';
    document.getElementById("product-description").value = '';
    document.getElementById("product-price").value = '';
    document.getElementById("product-location").value = '';
    document.getElementById("product-category").value = '';
    document.getElementById("product-images").value = '';
}

// Función de búsqueda por nombre
document.getElementById('search-input').addEventListener('input', function() {
    const query = this.value.toLowerCase();
    const filteredProducts = products.filter(product => product.name.toLowerCase().includes(query));
    const selectedCategory = document.getElementById('category-filter').value; // Obtiene la categoría seleccionada

    // Filtra por categoría si se selecciona una
    const finalFilteredProducts = filteredProducts.filter(product => {
        return selectedCategory === "" || product.category === selectedCategory;
    });

    displayProducts(finalFilteredProducts);
});

// Evento para el filtro de categorías
document.getElementById('category-filter').addEventListener('change', function() {
    const selectedCategory = this.value; // Obtiene la categoría seleccionada
    const searchQuery = document.getElementById('search-input').value.toLowerCase(); // Obtiene la búsqueda actual

    const filteredProducts = products.filter(product => {
        const matchesCategory = selectedCategory === "" || product.category === selectedCategory;
        const matchesQuery = product.name.toLowerCase().includes(searchQuery);
        return matchesCategory && matchesQuery; // Coincide con ambos
    });

    displayProducts(filteredProducts);
});

// Maneja la vista previa de la imagen del producto cuando se selecciona
document.getElementById("product-images").addEventListener("change", function(event) {
    const file = event.target.files[0]; // Obtiene el archivo de imagen seleccionado
    const preview = document.getElementById("image-preview"); // Obtiene el contenedor de vista previa de la imagen

    if (file) {
        const reader = new FileReader(); // Crea un objeto FileReader para leer el archivo
        reader.onload = function(e) {
            preview.src = e.target.result; // Establece la fuente de la imagen de vista previa
            preview.style.display = "block"; // Muestra la imagen de vista previa
        };
        reader.readAsDataURL(file); // Lee el archivo como una URL de datos
    } else {
        preview.src = ""; // Restablece la fuente si no hay archivo
        preview.style.display = "none"; // Oculta la vista previa si no hay imagen
    }
});




// Maneja la vista previa de la imagen del producto cuando se selecciona
document.getElementById("product-images").addEventListener("change", function(event) {
    const file = event.target.files[0]; // Obtiene el archivo de imagen seleccionado
    const preview = document.getElementById("image-preview"); // Obtiene el contenedor de vista previa de la imagen

    if (file) {
        const reader = new FileReader(); // Crea un objeto FileReader para leer el archivo
        reader.onload = function(e) {
            preview.src = e.target.result; // Establece la fuente de la imagen de vista previa
            preview.style.display = "block"; // Muestra la imagen de vista previa
        };
        reader.readAsDataURL(file); // Lee el archivo como una URL de datos
    } else {
        preview.src = ""; // Restablece la fuente si no hay archivo
        preview.style.display = "none"; // Oculta la vista previa si no hay imagen
    }
});



