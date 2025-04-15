document.addEventListener("DOMContentLoaded", () => {
    const counters = document.querySelectorAll(".counter-buttons")
    for (let i = 0; i < counters.length; i++) {
        let counter = counters[i]
        let inc_btn = counter.querySelector('.inc')
        let dec_btn = counter.querySelector('.dec')
        let number = counter.querySelector('.number')
        let min_unit = number.dataset.minUnit
        if (min_unit === null) {
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
        } else {
            inc_btn.addEventListener("click", () => {
              let current = parseInt(number.value, 10) || 0;
              number.value = current + 1;
            });
            dec_btn.addEventListener("click", () => {
              let current = parseInt(number.value, 10) || 0;
              const min = parseInt(number.min, 10) || 0;
              if (current > min) {
                number.value = current - 1;
              }
            });
        }

    }
})