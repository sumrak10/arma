document.addEventListener("DOMContentLoaded", () => {
    const sliders = document.getElementsByClassName("slider")
    for (let i = 0; i < sliders.length; i++) {
        var slider = sliders[i]
        let left_btn = slider.querySelector(".left_slider_button")
        let right_btn = slider.querySelector(".right_slider_button")
        let scroll_el = slider.querySelector(".scroll_element")
        left_btn.addEventListener("click", (e) => {
            scroll_el.scrollBy({
                left: -(window.innerWidth*0.5),
                behavior : "smooth"
            })
        })
        right_btn.addEventListener("click", (e) => {
            scroll_el.scrollBy({
                left: (window.innerWidth*0.5),
                behavior : "smooth"
            })
        })
    }
    const photo_sliders = document.getElementsByClassName("photo-slider")
    for (let i = 0; i < photo_sliders.length; i++) {
        var slider = photo_sliders[i]
        let left_btn = slider.querySelector(".left_slider_button")
        let right_btn = slider.querySelector(".right_slider_button")
        // let imgs = slider.querySelector(".sliding-imgs")
        let active_img = slider.querySelector(".active-img")
        let inactive_imgs = slider.querySelectorAll(".inactive-img")
        left_btn.addEventListener("click", (e) => {
            let current_id = parseInt(active_img.dataset.imgId) - 1
            if (current_id < 0) {
                current_id = inactive_imgs.length-1
            }
            active_img.dataset.imgId = current_id
            active_img.src = inactive_imgs[current_id].src
        })
        right_btn.addEventListener("click", (e) => {
            let current_id = parseInt(active_img.dataset.imgId) + 1
            if (current_id > inactive_imgs.length-1) {
                current_id = 0
            }
            active_img.dataset.imgId = current_id
            active_img.src = inactive_imgs[current_id].src
        })
    }
})