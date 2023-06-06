document.addEventListener("DOMContentLoaded", () => {
    if (document.querySelector("#put_in_basket-product-page")) {
        document.querySelector("#put_in_basket-product-page").addEventListener("click", (e) => {
            let data = new FormData()
            
            data.append("product_id", document.querySelector("#put_in_basket-product-page").getAttribute("product-id"))
            let count = parseInt(document.querySelector("#product-count").value)
            if (count === 0) {
                count = 1
            }
            data.append("count", count)
            let options = document.querySelectorAll(".option-for-basker-manager-js")
            let options_data = {}
            if (options.length != 0) {
                for (let j = 0; j < options.length; j++) {
                    let option = options[j]
                    let name = option.querySelector(".option-name").innerHTML
                    let value = ''
                    let vars = option.querySelectorAll(".option-var")
                    for (let k = 0; k < vars.length; k++) {
                        let var_ = vars[k]
                        if (var_.querySelector("input").checked) {
                            value = var_.querySelector("span").innerHTML
                        }
                    }
                    if (value === '') {
                        value = "Не выбран"
                    }
                    options_data[name] = value
                }
                data.append("options", JSON.stringify(options_data))
            }
            axios.post("/shop/put_in_basket", data)
            .then(result => {
                if (result['data']['status'] == 'added') {
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
            data.append("count", 1)
            axios.post("/shop/put_in_basket", data)
            .then(result => {
                if (result['data']['status'] == 'added') {
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