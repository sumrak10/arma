document.addEventListener("DOMContentLoaded", () => {
    let button = document.querySelector("#whatsapp-widget-button")
    let chat = document.querySelector("#whatsapp-widget-chat")
    let closechat = document.querySelector("#whatsapp-widget-close-chat")
    button.addEventListener("click", () => {
        if (chat.style.display === "none") {
            chat.style.display = "block"
        } else {
            chat.style.display = "none"
        }
    })
    closechat.addEventListener("click", () => {
        chat.style.display = "none"
    })
})
