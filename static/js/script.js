let old_values = {}
let output_elements_values = []

async function get_state() {
    const promise = await( await(await ( fetch(`/output_elements/state/`, {method: 'get'}))).json())
    // let values = promise

    // let day     =  new Date().getDate()
    // let hour    =  new Date().getHours()
    // let minute  =  new Date().getMinutes()
    // let second  =  new Date().getSeconds()
    // let mil_sec =  new Date().getMilliseconds()
    
    // let time = `${day}:${hour}:${minute}:${second}:${mil_sec}`
    // //console.log("---------------")
    // values["time"] = `${time}`
    // output_elements_values.push(JSON.stringify(values))
    // //output_elements_values.forEach(element => console.log(element))

    return promise
}

async function set_state(values) {
    //console.log(values)
    let p = await fetch(`/input_elements/state/`, {
        method: 'POST', 
        headers: {
            'Accept': 'application/json',
            'Content-type': 'application/json'
        },
        body: JSON.stringify(values)
    });
    return "complete"
}

function update_ui() {
    document.querySelectorAll(".input-range").forEach(element => {
        let max = element.querySelector(".form-range").max
        let value = element.querySelector(".form-range").value
        element.querySelector(".value-max").innerHTML = `${value} / ${max}`
        })
    }
    
    function update() {
        let values = {}
        let output_values = {}
        get_state().then(elements => {
        output_values = elements
        document.querySelectorAll(".output-element").forEach(element => {
            element.querySelector(".value").innerHTML = output_values[element.querySelector(".name").innerHTML]
            })
        document.querySelectorAll(".element").forEach(element => {
            if(element.classList[1] == "input-bool") {
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
            }    
        })

        document.querySelectorAll(".special-element-group").forEach(element => {
            let special_values = {}
            let element_name = element.querySelector(".special-name").innerHTML
            element.querySelectorAll(".special-element").forEach(element => {
                if(element.classList[1] == "input-bool") {
                    let name = element.querySelector(".name").innerHTML
                    let value = element.querySelector(".form-check-input").checked
                    special_values[name] = value
                }
                else if(element.classList[1] == "input-text") {
                    let name = element.querySelector(".name").innerHTML
                    let value = element.querySelector(".form-control").value
                    special_values[name] = value
                }
                else if(element.classList[1] == "input-range") {
                    let name = element.querySelector(".name").innerHTML
                    let value = element.querySelector(".form-range").value
                    special_values[name] = value
                }
            })
            values[element_name] = special_values
        })

    if (JSON.stringify(old_values) != JSON.stringify(values)) {
        //console.log("new_values",values, old_values)
        old_values = values
        set_state(values)
        }
    })
}

setInterval(() => {update_ui()}, 100)
setInterval(() => {update()}, 1000)