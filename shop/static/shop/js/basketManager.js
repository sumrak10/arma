document.addEventListener("DOMContentLoaded", () => {


    if (localStorage.getItem("basket") && localStorage.getItem("basket") != '{}') {
        console.log(localStorage.getItem("basket"))
        document.getElementById("basket-data").value = localStorage.getItem("basket");
        document.getElementById("basket-not-empty").style.display = "block";
        
    } else {
        document.getElementById("basket-not-empty").style.display = "none";
    }

    const elements = document.getElementsByClassName("put_in_basket");

    for (let i = 0; i < elements.length; i++) {
        let basket = {};
        if (localStorage.getItem("basket")) {
            basket = JSON.parse(localStorage.getItem("basket"));
        }
        const productId = elements[i].getAttribute("product_id");
        if (basket.hasOwnProperty(productId)) {
            console.log(elements[i])
            elements[i].innerHTML = "В корзине"
            elements[i].style.backgroundColor = "#414141"
        }
    }
    
    for (let i = 0; i < elements.length; i++) {
    elements[i].addEventListener("click", function() {
        let basket = {};
        if (localStorage.getItem("basket")) {
            basket = JSON.parse(localStorage.getItem("basket"));
        }
        const productId = this.getAttribute("product_id");
        if (basket.hasOwnProperty(productId)) {
            delete basket[productId];
            this.innerHTML = "В корзину"
            this.style.backgroundColor = "#CC0000"
        } else {
            basket[productId] = 1;
            this.innerHTML = "В корзине"
            this.style.backgroundColor = "#414141"

        }
        localStorage.setItem("basket", JSON.stringify(basket));
        if (localStorage.getItem("basket") == '{}') {
            document.getElementById("basket-not-empty").style.display = "none";
        } else {
            document.getElementById("basket-not-empty").style.display = "block";
        }
        document.getElementById("basket-data").value = localStorage.getItem("basket");
    });
    }

})