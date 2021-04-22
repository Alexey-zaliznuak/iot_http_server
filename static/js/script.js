const menu = `

<nav class="navbar navbar-expand-lg navbar-light" style = "justify-content:space-beetwen;  padding: 0 0 0 5%">
    <label class="navbar-brand" style = 'font-size:25px;'>Element-conroller</label>
    <a href = "/"><label class = "menu-label">History</label><a>
</nav>
`
async function init() {
    const content = await (await fetch(`/content`, {method: 'get'})).text()
    document.body.innerHTML = menu + content
}
init()