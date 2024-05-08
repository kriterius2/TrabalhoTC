function validarNome() {
    const nome = document.getElementById('nome').value;
    const resultado = document.getElementById('resultado');
    const nomeRegex =new RegExp(`^[${Gama}][${Epsilon}]+(\\s[${Gama}][${Epsilon}]+){1,2}$`);

    if (nomeRegex.test(nome)) {
        resultado.textContent = 'Nome válido!';
        resultado.style.color = 'green';
    } else {
        resultado.textContent = 'Nome inválido!';
        resultado.style.color = 'red';
    }
}

function validarEmail() {
    const email = document.getElementById('email').value;
    const resultado = document.getElementById('resultado');
    const emailRegex = new RegExp(`^[${Epsilon}${Gama}${Nu}._%+-]+@[${Epsilon}${Gama}${Nu}.-]+\.[${Epsilon}${Gama}]{2,}$`);

    if (emailRegex.test(email)) {
        resultado.textContent = 'E-mail válido!';
        resultado.style.color = 'green';
    } else {
        resultado.textContent = 'E-mail inválido!';
        resultado.style.color = 'red';
    }
}

function validarSenha() {
    const senha = document.getElementById('senha').value;
    const resultado = document.getElementById('resultado');
    const senhaRegex = new RegExp(`^(?=.*[${Gama}])(?=.*[${Nu}])[${Epsilon}${Gama}${Nu}]*[${Epsilon}${Gama}${Nu}]*$`);

    if (senhaRegex.test(senha)) {
        resultado.textContent = 'Senha válida!';
        resultado.style.color = 'green';
    } else {
        resultado.textContent = 'Senha inválida!';
        resultado.style.color = 'red';
    }
}

function validarCPF() {
    const cpf = document.getElementById('cpf').value;
    const resultado = document.getElementById('resultado');
    const cpfRegex = new RegExp(`^[${Nu}]{3}.[${Nu}]{3}.[${Nu}]{3}-[${Nu}]{2}$`);

    if (cpfRegex.test(cpf)) {
        resultado.textContent = 'CPF válido!';
        resultado.style.color = 'green';
    } else {
        resultado.textContent = 'CPF inválido!';
        resultado.style.color = 'red';
    }
}

function validarTelefone() {
    const telefone = document.getElementById('telefone').value;
    const resultado = document.getElementById('resultado');
    const telefoneRegex = new RegExp(`^\\({0,1}[${Nu}]{2}\\){0,1}\\s9[${Nu}]{4}-{0,1}[${Nu}]{4}$`);

    if (telefoneRegex.test(telefone)) {
        resultado.textContent = 'Telefone válido!';
        resultado.style.color = 'green';
    } else {
        resultado.textContent = 'Telefone inválido!';
        resultado.style.color = 'red';
    }
}

function validarData() {
    const data = document.getElementById('data').value;
    const resultado = document.getElementById('resultado');
    const dataRegex = new RegExp(`^[${Nu}][${Nu}]\/[${Nu}][${Nu}]\/[${Nu}][${Nu}][${Nu}][${Nu}]\\s[0-2][${Nu}]\:[0-5][${Nu}]\:[0-5][${Nu}]$`);

    if (dataRegex.test(data)) {
        resultado.textContent = 'Data válida!';
        resultado.style.color = 'green';
    } else {
        resultado.textContent = 'Data inválida!';
        resultado.style.color = 'red';
    }
}

function validarNumero() {
    const telefone = document.getElementById('numero').value;
    const resultado = document.getElementById('resultado');
    const numeroRegex = new RegExp(`^[+|-]{0,1}[${Nu}]+(\.[${Nu}]+)?$`);

    if (numeroRegex.test(telefone)) {
        resultado.textContent = 'Mumero válido!';
        resultado.style.color = 'green';
    } else {
        resultado.textContent = 'Numero inválido!';
        resultado.style.color = 'red';
    }
}
