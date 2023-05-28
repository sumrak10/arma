document.addEventListener("DOMContentLoaded", () => {
    // console.log(localStorage.getItem("basket"))
    // КРАСНЫЙ БЭДЖИК В ХЕАДЕРЕ У КНОПКИ "КОРЗИНА"
    if (localStorage.getItem("basket") && localStorage.getItem("basket") != '{}') {
        document.getElementById("basket-data").value = localStorage.getItem("basket");
        document.getElementById("basket-not-empty").style.display = "block";
        
    } else {
        document.getElementById("basket-not-empty").style.display = "none";
    }


    // ОТРИСОВКА КНОПОК В НУЖНОМ СОСТОЯНИИ НА СТРАНИЦЕ С ПРОДУКТАМИ (/category)
    const elements = document.getElementsByClassName("put_in_basket");
    for (let i = 0; i < elements.length; i++) {
        var basket = {};
        if (localStorage.getItem("basket")) {
            basket = JSON.parse(localStorage.getItem("basket"));
        }
        var productId = elements[i].getAttribute("product-id");
        if (basket.hasOwnProperty(productId)) {
            elements[i].innerHTML = "В корзине"
            elements[i].classList.toggle("product-card-buttons-in-basket-active")
        }
    }
    
    // СОБЫТИЯ НА КНОПКИ У ТОВАРОВ НА СТРАНИЦЕ С ПРОДУКТАМИ
    for (let i = 0; i < elements.length; i++) {
    elements[i].addEventListener("click", function() {
        var basket = {};
        if (localStorage.getItem("basket")) {
            basket = JSON.parse(localStorage.getItem("basket"));
        }
        var productId = this.getAttribute("product-id");
        if (basket.hasOwnProperty(productId)) {
            delete basket[productId];
            this.innerHTML = "В корзину"
            this.classList.toggle("product-card-buttons-in-basket-active")
        } else {
            basket[productId] = 1;
            this.innerHTML = "В корзине"
            this.classList.toggle("product-card-buttons-in-basket-active")

        }
        // обновляем бэджик у кнопки корзины в хеадере и сохраняем корзину в локальное хранилище
        localStorage.setItem("basket", JSON.stringify(basket));
        if (localStorage.getItem("basket") == '{}') {
            document.getElementById("basket-not-empty").style.display = "none";
        } else {
            document.getElementById("basket-not-empty").style.display = "block";
        }
        document.getElementById("basket-data").value = localStorage.getItem("basket");
    });
    }
    // ОТРИСОВКА КНОПОК В НУЖНОМ СОСТОЯНИИ НА СТРАНИЦЕ САМОГО ТОВАРА
    const element = document.querySelector("#put-in-basket")
    const counter = document.querySelector("#product-count")
    if (element) {
        var basket = {};
        if (localStorage.getItem("basket")) {
            basket = JSON.parse(localStorage.getItem("basket"));
        }
        var productId = element.getAttribute("product-id");
        if (basket.hasOwnProperty(productId)) {
            element.innerHTML = "Уже в корзине"
            element.classList.toggle("product-card-buttons-in-basket-active")
            counter.value = basket[productId]
        }
    

    // СОБЫТИЕ НА КНОПКУ НА СТРАНИЦЕ САМОГО ТОВАРА
    document.querySelector("#put-in-basket").addEventListener("click", function() {
        var basket = {};
        if (localStorage.getItem("basket")) {
            basket = JSON.parse(localStorage.getItem("basket"));
        }
        var count = document.querySelector("#product-count").value
        var productId = this.getAttribute("product-id");
        if (basket.hasOwnProperty(productId)) {
            delete basket[productId];
            this.innerHTML = "Добавить в корзину"
            this.classList.toggle("product-card-buttons-in-basket-active")
        } else {
            basket[productId] = count;
            this.innerHTML = "Уже в корзине"
            this.classList.toggle("product-card-buttons-in-basket-active")
        }

        // обновляем бэджик у кнопки корзины в хеадере и сохраняем корзину в локальное хранилище
        localStorage.setItem("basket", JSON.stringify(basket));
        if (localStorage.getItem("basket") == '{}') {
            document.getElementById("basket-not-empty").style.display = "none";
        } else {
            document.getElementById("basket-not-empty").style.display = "block";
        }
        document.getElementById("basket-data").value = localStorage.getItem("basket");
    })
    }

})