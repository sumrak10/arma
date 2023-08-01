document.addEventListener("DOMContentLoaded", () => {
    
    document.querySelector("#header__consultation_button").addEventListener("click", (e) => {
        document.querySelector(".header-consultation__wrapper").classList.toggle("header-consultation__wrapper_opened")
    })
    document.querySelector(".header-consultation-form_close").addEventListener("click", (e) => {
        document.querySelector(".header-consultation__wrapper").classList.remove("header-consultation__wrapper_opened")
    })
})