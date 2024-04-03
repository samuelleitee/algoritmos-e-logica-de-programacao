function passwordGenerate(){
    document.getElementById('resposta').value = ''
    let length = document.getElementById('passwordLength').value;
    let quantity = document.getElementById('passwordNumber').value;
    let specialCharacter = document.getElementById('caracteresEspeciais').checked;
    let numericCharacter = document.getElementById('numeros').checked;
    let upperCharacter = document.getElementById('letrasMaiusculas').checked;
    let caracteres = 'abcdefghijklmnopqrstuvwxyz'

    if(specialCharacter){
        caracteres += '!@#$%&*()?'
    }
    if(numericCharacter){
        caracteres += '0123456789'
    }
    if(upperCharacter){
        caracteres += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    }

    for(let i = 0; i < quantity; i++){
        let senha = '';
        for(let i = 0; i < length; i++){

            var aleatorio = Math.floor(Math.random() * caracteres.length)
            senha += caracteres.substring(aleatorio, aleatorio + 1)
        }
        document.getElementById('resposta').value += senha + '\n'
    }
}

function clearPassword(){
    document.getElementById('passwordLength').value = '';

    document.getElementById('passwordNumber').value = '';

    document.getElementById('caracteresEspeciais').checked = false

    document.getElementById('numeros').checked = false

    document.getElementById('letrasMaiusculas').checked = false

    document.getElementById('resposta').value = 'Senha...';
}