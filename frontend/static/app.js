const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const messagesBox = document.getElementById("messages");
const statusBox = document.getElementById("status");
const sendButton = document.getElementById("send-button");

function appendMessage(text, type) {
    const item = document.createElement("div");
    item.className = `message ${type}`;
    item.textContent = text;
    messagesBox.appendChild(item);
    messagesBox.scrollTop = messagesBox.scrollHeight;
}

async function sendMessage(message) {
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
    });

    if (!response.ok) {
        throw new Error("No se pudo procesar la consulta.");
    }

    return response.json();
}

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();
    if (!message) {
        return;
    }

    appendMessage(`Usuario: ${message}`, "message-user");
    messageInput.value = "";
    messageInput.focus();
    sendButton.disabled = true;
    statusBox.textContent = "Procesando...";

    try {
        const data = await sendMessage(message);
        appendMessage(`Chatbot: ${data.answer}`, "message-bot");
        statusBox.textContent = data.matched
            ? "Respuesta encontrada en la base actual de FAQs."
            : "No hubo coincidencia exacta; se devolvio el fallback controlado.";
    } catch (error) {
        appendMessage(
            "Error: no se pudo conectar con el servicio de chat. Intentalo de nuevo.",
            "message-error",
        );
        statusBox.textContent = "Se produjo un error durante la peticion.";
    } finally {
        sendButton.disabled = false;
    }
});
