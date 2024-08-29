let socket = new WebSocket("ws://localhost:8000/ws");

socket.onmessage = function (event) {
    let messages = document.getElementById("messages");
    let message = document.createElement("p");
    message.textContent = event.data;
    messages.appendChild(message);
};

function sendMessage() {
    let message = "Hello, server!";
    socket.send(message);
}
