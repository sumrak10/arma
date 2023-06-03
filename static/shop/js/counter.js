document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll(".counter-buttons")
    for (let i = 0; i < counters.length; i++) {
        var counter = counters[i]
        let inc_btn = counter.querySelector('.inc')
        let dec_btn = counter.querySelector('.dec')
        let number = counter.querySelector('.number')
        inc_btn.addEventListener("click", (e) => {
            number.value++
        })
        dec_btn.addEventListener("click", (e) => {
            if (number.value > 0) {
                number.value--
            }
        })
    }
})