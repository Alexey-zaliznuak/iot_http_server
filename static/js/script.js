let old_values = {}

async function seet_state(id, state) {
    //console.log(element)
    let p = await fetch(`/State/${id}/${state}`, {method: 'post'})
    const promise = await (await fetch(`/State/${id}`, {method: 'get'})).text()
    Update_button(promise, id)
    //then(req => req.text().then((text) => hello(text, id)))
    return promise
}
function update() {
    let values = {}
    document.querySelectorAll(".element-container").forEach(element => {
        if (element.classList[1] == "output") {
            let name = element.querySelector(".element-name").innerHTML
            let value = element.querySelector(".value").innerHTML
            values[name] = value
        }
        else if(element.classList[1] == "input-bool") {
            let name = element.querySelector(".name").innerHTML
            let value =element.querySelector(".form-check-input").checked
            values[name] = value
        }
        else if(element.classList[1] == "input-text") {
            let name = element.querySelector(".name").innerHTML
            let value = element.querySelector(".form-control").value
            values[name] = value
        }
        else if(element.classList[1] == "input-range") {
                let name = element.querySelector(".name").innerHTML
                let value = element.querySelector(".form-range").value
                values[name] = value

                let max = element.querySelector(".form-range").max
                element.querySelector(".value-max").innerHTML = `${value} / ${max}`
        }})
    if (JSON.stringify(old_values) != JSON.stringify(values)) {
        //console.log("new_values",values, old_values)
        old_values = values
        set_state(values)
    }
}
async function set_state(values) {
    //console.log(element)
    console.log(values)
    let p = await fetch(`/State/`, {
        method: 'POST', 
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        },
        body: JSON.stringify(values)
    });
    return "complete"
    //then(req => req.text().then((text) => hello(text, id)))
}

function updates() {
    setInterval(() => {
    update()
}, 50);}

updates()