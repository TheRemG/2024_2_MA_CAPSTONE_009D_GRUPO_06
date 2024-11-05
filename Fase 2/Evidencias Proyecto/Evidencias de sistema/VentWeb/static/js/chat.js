function sendMessage() {
    const input = document.getElementById("chat-input");
    const message = input.value.trim();
    if (message) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message");
        messageElement.textContent = message;
        document.getElementById("messages").appendChild(messageElement);
        input.value = ""; // Limpia el campo de entrada
    }
}

