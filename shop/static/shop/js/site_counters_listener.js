document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll(".counter-buttons")
    for (let i = 0; i < counters.length; i++) {
        var counter = counters[i]
        let inc_btn = counter.querySelector('.inc')
        let dec_btn = counter.querySelector('.dec')
        let number = counter.querySelector('.number')
        let min_unit = number.getAttribute('min-unit')
        inc_btn.addEventListener("click", (e) => {
            number.value = ((number.value / min_unit) + 1) * min_unit

        })
        dec_btn.addEventListener("click", (e) => {
            if (number.value > 0) {
                number.value = ((number.value / min_unit) - 1) * min_unit
            }
        })
        number.addEventListener("change", (e) => {
            number.value = Math.round(number.value/min_unit) * min_unit
        })
    }
})