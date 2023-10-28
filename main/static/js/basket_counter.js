document.addEventListener("DOMContentLoaded", () => {
    computeBasketButtonCounter()
})

function computeBasketButtonCounter() {
    axios.get("/shop/products_in_basket_count")
    .then(result => {
        let count = parseInt(result['data']['count'])
        document.querySelector('#basket-not-empty').innerHTML = count
        autoHideBasketButtonCounter(count)
    })
    .catch(error => {
        console.log(error)
    })
}

function incBasketButtonCounter() {
    count = parseInt(document.querySelector('#basket-not-empty').innerHTML)
    document.querySelector('#basket-not-empty').innerHTML = count + 1
    autoHideBasketButtonCounter(count+1)
}

function decBasketButtonCounter() {
    count = parseInt(document.querySelector('#basket-not-empty').innerHTML)
    document.querySelector('#basket-not-empty').innerHTML = count - 1
    autoHideBasketButtonCounter(count-1)
}

function autoHideBasketButtonCounter(count) {
    if (count == 0) {
        document.querySelector('#basket-not-empty').style.display = "none"
    } else {
        document.querySelector('#basket-not-empty').style.display = "block"
    }
}