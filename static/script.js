function sendMessage() {
    const input = document.getElementById("message");
    const message = input.value;
    if (!message) return;

    addMessage(message, "user");

    fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.response, "bot");
    });

    input.value = "";
}

function addMessage(text, type) {
    const chatBox = document.getElementById("chat-box");
    const div = document.createElement("div");
    div.className = "message " + type;
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function newChat() {
    document.getElementById("chat-box").innerHTML = "";
}
