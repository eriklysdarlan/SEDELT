
function handleClick(event) {
    
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        let value = button.getAttribute("aria-selected");
        button.setAttribute("aria-selected", (value == "true") ? "false" : "true");
    });
    
    return window.location.href = event
}