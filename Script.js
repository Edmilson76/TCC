const botao = document.querySelector("#botao");
const tabela = document.querySelector("#tabela-iphone");

botao.addEventListener('click', function() {
    carregarDados();

})

function carregarDados() {
    fetch('http://127.0.0.1:5000/todos')
    .then(function(resposta) {
        return resposta.json();
    })
    .then(function(ListaIphone) {
      popularTabela(ListaIphone);
       
    })
}
function popularTabela(listaIphone){
    const tamanhoLista = listaIphone.length;
    
    for(let index = 0; index < tamanhoLista; index++) {
        const linha = document.createElement('tr');

        const id = document.createElement('td'); 
        const Modelo = document.createElement('td'); 
        const Capacidade = document.createElement('td'); 
        const preco = document.createElement('td'); 

        id.innerHTML = listaIphone[index][0];
        Modelo.innerHTML = listaIphone[index][1];
        Capacidade.innerHTML = listaIphone[index][2];
        preco.innerHTML = listaIphone[index][3];
        
        linha.appendChild(id); 
        linha.appendChild(Modelo);
        linha.appendChild(Capacidade);
        linha.appendChild(preco);    
        tabela.appendChild(linha);
    }
    
}