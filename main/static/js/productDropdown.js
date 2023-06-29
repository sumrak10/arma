document.addEventListener("DOMContentLoaded", () => {
    for (let i = 0; i < document.querySelectorAll(".product-card_with-options").length; i++) {
        document.querySelectorAll(".product-card_with-options")[i].querySelector('.dropdown__button').addEventListener("click", () => {
            document.querySelectorAll(".product-card_with-options")[i].querySelector('.dropdown__list').classList.toggle("dropdown__list_active")
            for (let j=0; j<document.querySelectorAll(".product-card_with-options")[i].querySelectorAll('.dropdown__list__item').length; j++) {
                document.querySelectorAll(".product-card_with-options")[i].querySelectorAll('.dropdown__list__item')[j].addEventListener("click", () => {
                    document.querySelectorAll(".product-card_with-options")[i].querySelector('.dropdown__list').classList.remove("dropdown__list_active")
                    let txt = document.querySelectorAll(".product-card_with-options")[i].querySelectorAll('.dropdown__list__item')[j].innerHTML
                    document.querySelectorAll(".product-card_with-options")[i].querySelector('.dropdown__button__text').innerHTML = txt
                    if (!document.querySelectorAll(".product-card_with-options")[i].classList.contains("product-card_null-price")) {
                        console.log("xfg")
                        let r_price = document.querySelectorAll(".product-card_with-options")[i].querySelectorAll('.dropdown__list__item')[j].getAttribute("r-price")
                        document.querySelectorAll(".product-card_with-options")[i].querySelector('.product-card-r-price').innerHTML = r_price + " ₽"
                        let d = document.querySelectorAll(".product-card_with-options")[i].querySelectorAll('.dropdown__list__item')[j].getAttribute("o-price")
                        console.log(d, r_price)
                        let o_price = parseInt(r_price) + (r_price*d/100)
                        document.querySelectorAll(".product-card_with-options")[i].querySelector('.product-card-old-price').innerHTML = o_price + " ₽"
                    }
                })
            }
        })
    }
})