function somar(){
    var numero1 = parseInt(document.getElementById('numero1').value)
    var numero2 = parseInt(document.getElementById('numero2').value)
    var soma = numero1 + numero2
    document.getElementById('resultado').innerHTML = 'Resultado: ' + numero1 + ' + ' + numero2 + ' = ' + soma
    // innerHTML: Serve para escrever algo dentro de um elemento. 
}