const botao = document.querySelector("#botao");
const tabela = document.querySelector("#tabela-aluno");

botao.addEventListener('click', function() {
    carregarDados();

})

fetch('http//127.0.0.1:5000/todos')
    .then(function(resposta) {
        return resposta.json()
    }).then(function(ListaAluno)
    {  console.log(ListaAluno);
    })

function popularTabela(listaAluno){
    const tamanhoLista = listaAluno.length;
    
    for(let index = 0; index < tamanhoLista; index++) {
        console.log(listaAluno[index]);
        const id = document.createElement('td'); 
        const Modelo = document.createElement('td'); 
        const Capacidade = document.createElement('td'); 
        const preco = document.createElement('td'); 
        id.innerHTML = listaAluno[index][0];
        Modelo.innerHTML = listaAluno[index][1];
        Capacidade.innerHTML = listaAluno[index][2];
        preco.innerHTML = listaAluno[index][3];
        
        linha.appendChild(id);
        linha.appendChild(Modelo);
        linha.appendChild(Capacidade);
        linha.appendChild(preco)
     
    }
    
}