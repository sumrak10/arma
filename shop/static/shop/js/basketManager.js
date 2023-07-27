document.addEventListener("DOMContentLoaded", () => {
    if (document.querySelector("#put_in_basket-product-page")) {
        document.querySelector("#put_in_basket-product-page").addEventListener("click", (e) => {
            let data = new FormData()
            
            if (document.querySelector(".option-var-active") != null) {
                data.append("option_id", document.querySelector(".option-var-active").getAttribute("option-id"))
            } 
            data.append("product_id", document.querySelector("#put_in_basket-product-page").getAttribute("product-id"))
            let count = parseInt(document.querySelector("#product-count").value)
            if (count === 0) {
                count = document.querySelector("#put_in_basket-product-page").getAttribute("min-unit")
            }
            data.append("count", count)
            axios.post("/shop/put_in_basket", data)
            .then(result => {
                if (result['data']['status'] == 'added') {
                    ym(94231080,'reachGoal','inBasket')
                    document.querySelector("#put_in_basket-product-page").innerHTML = "Убрать из корзины"
                    document.querySelector("#put_in_basket-product-page").classList.add("in_basket-active")
                    console.log("добавлен")
                } else {
                    document.querySelector("#put_in_basket-product-page").innerHTML = "В корзину"
                    document.querySelector("#put_in_basket-product-page").classList.remove("in_basket-active")
                    console.log("удален")
                }
            })
            .catch(error => {
                console.log("error")
            })
        })
    }
    c_buttons = document.querySelectorAll(".put_in_basket-category-page")
    for (let i=0; i < c_buttons.length; i++) {
        c_buttons[i].addEventListener("click", (e) => {
            let data = new FormData()
            data.append("product_id", c_buttons[i].getAttribute("product-id"))
            data.append("count", c_buttons[i].getAttribute("min-unit"))
            axios.post("/shop/put_in_basket", data)
            .then(result => {
                if (result['data']['status'] == 'added') {
                    ym(94231080,'reachGoal','inBasket')
                    c_buttons[i].innerHTML = "В корзине"
                    c_buttons[i].classList.add("product-card-buttons-in-basket-active")
                } else {
                    c_buttons[i].innerHTML = "В корзину"
                    c_buttons[i].classList.remove("product-card-buttons-in-basket-active")
                }
            })
            .catch(error => {
                console.log("error")
            })
        })
    }
})