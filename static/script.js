function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");

    if (sidebar.style.left === "0px") {
        sidebar.style.left = "-250px";
    } else {
        sidebar.style.left = "0px";
    }
}

function newChat() {
    alert("تم بدء دردشة جديدة");
}

function logout() {
    window.location.href = "/logout";
}
