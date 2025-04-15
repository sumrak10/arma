document.addEventListener("DOMContentLoaded", function () {
    const phoneInputs = document.querySelectorAll(".form-phone");
    Inputmask({
        mask: "+7 (999) 999-99-99",
        showMaskOnHover: false,
        showMaskOnFocus: true,
        clearIncomplete: false,
    }).mask(phoneInputs)

    const consultationPopupContainer = document.querySelector("#consultation_popup_container");
    consultationPopupContainer.addEventListener("click", function (e) {
        if (e.target.classList.contains("consultation-popup-container")) {
            consultationPopupContainer.classList.remove('active');
        }
    });
    const consultationPopupCloseBtn = document.querySelector("#consultation_popup_close_btn");
    consultationPopupCloseBtn.addEventListener("click", function () {
        consultationPopupContainer.classList.remove('active');
    });
    const consultationPopupOpenBtns = document.querySelectorAll(".consultation-popup-open-btn");
    consultationPopupOpenBtns.forEach((elem) => {
        elem.addEventListener('click', () => {
            console.log("clicked");
            consultationPopupContainer.classList.add('active');
        });
    });

    const getOptPopupContainer = document.querySelector("#get_opt_popup_container");
    getOptPopupContainer.addEventListener("click", function (e) {
        if (e.target.classList.contains("consultation-popup-container")) {
            getOptPopupContainer.classList.remove('active');
        }
    });
    const getOptPopupCloseBtn = document.querySelector("#get_opt_popup_close_btn");
    getOptPopupCloseBtn.addEventListener("click", function () {
        getOptPopupContainer.classList.remove('active');
    });
    const getOptPopupOpenBtns = document.querySelectorAll(".get-opt-popup-open-btn");
    getOptPopupOpenBtns.forEach((elem) => {
        elem.addEventListener('click', () => {
            console.log("clicked");
            getOptPopupContainer.classList.add('active');
        });
    });
});