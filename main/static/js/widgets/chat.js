document.addEventListener("DOMContentLoaded", () => {
    var first_message = true

    var chat_widget = document.querySelector(".chat-widget")
    var chat_widget_messages_list = document.querySelector(".chat-widget__messages-list")
    var chat_widget_button = document.querySelector(".chat-widget-button")

    // close and open widget controls 
    var chat_widget_close_button = document.querySelector(".chat-widget__header__close-button")
    chat_widget_button.addEventListener('click', (e) => {
        chat_widget.classList.toggle("chat-widget___inactive")
        chat_widget_button.classList.toggle("chat-widget___inactive")
    })
    chat_widget_close_button.addEventListener('click', (e) => {
        chat_widget.classList.toggle("chat-widget___inactive")
        chat_widget_button.classList.toggle("chat-widget___inactive")
    })

    // downloading history 
    // add_message('manager', text='Привет', time='12:05')
    // add_message('client', text='Привет', time='12:06')
    // add_message('status', text='Привет')


    // Прокрутка по умолчанию
    chat_widget_messages_list.scrollTo(0,chat_widget_messages_list.scrollHeight)

    // send message event
    document.querySelector("#widget-form-send-message-button").addEventListener('click', (e) => {
        e.preventDefault()
        first_message = send_message(first_message)
    })
    document.querySelector("#widget-form-send-message-text").addEventListener('keydown', (e) => {
        if (e.keyCode === 13) {
            first_message = send_message(first_message)
        }
    })
})

function send_message(first_message) {
    let text = document.querySelector("#widget-form-send-message-text").value
    document.querySelector("#widget-form-send-message-text").value = ''
    add_message('client', text=text)
    if (first_message) {
        first_message = false
        ws = websocket(text)
    } else {
        data = {
            "command": "message",
            "text": text
        }
        ws.send(JSON.stringify(data))
    }
    return first_message
}

function websocket(first_message_text) {
    var ws = new WebSocket("wss://arma72vps.ru:443/bot/crm/chat_widget/ws");
    ws.onopen = function(e) {
        console.log("Соединение открыто")
        add_message(state='status', text='Специалист уточняет информацию по вашему запросу')
        data = {
            "command": "first_message",
            "uid":get_cookie("csrftoken"),
            "text": first_message_text
        }
        ws.send(JSON.stringify(data))
    }
    ws.onmessage = function (e) {
        data = JSON.parse(e.data)
        console.log(data)
        console.log(typeof(data))
        if (data['command'] === 'room_created') {
            console.log("sdf")
        } else if (data['command'] === 'message') {
            add_message('manager', text=data['text'])
        }
        
    }
    ws.onclose = function (e) {
        if (e.wasClean) {
            console.log("Соединение закрыто правильно")
            add_message('status', text="Онлайн консультация окончена. Перезагрузите страницу если хотите задать новый вопрос.")
        } else {
            console.log("Соедениние прервано")
            add_message('status', text="Соединение прервано. Перезагрузите страницу и попробуйте снова")
        }
    }
    ws.onerror = function (e) {
        console.log(e)
    }
    return ws
}



// utils

function get_cookie(name) {
    cookies = get_cookies_map()
    return cookies.get(name)
}

function get_cookies_map() {
    let cookies = new Map();
    for( let cookie of document.cookie.split(";") ) {
        // Split the elements at "="
        cookie = cookie.split( "=" )
        // Set the first element as key and second element as value
        cookies.set( cookie[0].replace(" ",""), cookie[1] )
    }
    return cookies
}

function time_now() {
    let now = new Date()
    let time = now.toLocaleTimeString([], {hour: "2-digit", minute: "2-digit"})
    return time
}

function add_message(state, text) {
    document.querySelector(".chat-widget__messages-list").appendChild(build_message_element(state,text,time_now()))
}

function build_message_element(state, text, time='') {
    let message = document.createElement('div')
    message.classList.add("chat-widget__message-wrapper")
    message.innerHTML = '<div class="chat-widget__message"><div class="chat-widget__message__text">'+text+'</div><div class="chat-widget__message__datetime">'+time+'</div></div>'
    if (state=="client") {
        message.classList.add("chat-widget__message___client")
    }
    else if (state=="manager") {
        message.classList.add("chat-widget__message___manager")
    } else if (state=="status") {
        message.innerHTML = text
        message.classList.add("chat-widget__message___status")
    }
    return message
}