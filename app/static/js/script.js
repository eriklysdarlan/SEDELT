const usarFetch = document.getElementById('usarFetch')

usarFetch.addEventListener('click', function() {
    console.log(url)
    fetch(url)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            //document.getElementById('output').innerHTML = dados['nome'];
        })
        .catch(error => console.error('Error:', error))
})