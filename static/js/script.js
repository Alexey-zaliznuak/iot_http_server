function time_update() {
    var hour = new Date().getHours()
    var minute = new Date().getMinutes()

    if (hour < 10) {
        hour = `0${hour}`
    }
    
    if (minute < 10) {
        minute = `0${minute}`
    }

    document.querySelector(".time").innerHTML = `${hour}:${minute}`
    setTimeout(time_update, 1000)
}

document.addEventListener('click', event => {
    const element = event.target;
    const is_control_element = element.classList.contains('control_element')
    state = ''

    if (element.innerHTML == "on") {
        state = "off"
    }
    else {
        state = "on"
    }
    
    if (is_control_element) {
        id = element.id
        set_state(id, state, element)
    }
})

function hello(res, id) {
    console.log(res, id)
    document.getElementById(id).innerHTML = res
    return res, id
}

function set_state(id, state, element) {
    //console.log(element)
    let p = fetch(`http://127.0.0.1:5000/SetState/${id}/${state}`, {method: 'get'})
    let promise = fetch(`http://127.0.0.1:5000/GetState/${id}`, {method: 'get'}).then(req => req.text().then((text) => hello(text, id)))
    return promise
}


time_update()