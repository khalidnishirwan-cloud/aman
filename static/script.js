function sendMessage() {
    const input = document.getElementById("message");
    const msg = input.value;

    if (!msg) return;

    addMessage(msg, "user");

    fetch('/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.response, "bot");
    });

    input.value = "";
}

function addMessage(text, type) {
    const box = document.getElementById("chat-box");

    const div = document.createElement("div");
    div.className = "message " + type;
    div.innerText = text;

    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}

function newChat() {
    document.getElementById("chat-box").innerHTML = "";
}

function goLogin() {
    window.location.href = "/login";
}

function goRegister() {
    window.location.href = "/register";
}
