function trocarpalavra() {
    document.getElementById("green-green-grass-of-home").innerHTML = 'verde verde grama da casa';
}

function modoEscuro() {
  document.body.style.backgroundColor = "#222222";

  document.getElementById("green-green-grass-of-home").style.color = "white";
}

function entrar() {

  let nomeDigitado = document.getElementById("campo-nome").value;
  let senhaDigitada = document.getElementById("campo-senha").value;

  if (senhaDigitada === "1234") {

    alert("Bem-vindo(a) ao Site, " + nomeDigitado + "!");
  } else {
    alert("Senha Incorreta!, esta senha ja foi utilizada") // KKKKKso pra zuar
  } 
}


function mostrarCadastro() {
  document.getElementById("area-login").style.display = "none";
  document.getElementById("area-cadastro").style.display = "block";

}

function mostrarLogin() {
  document.getElementById("area-cadastro").style.display= "none";
  document.getElementById("area-login").style.display = "block";

}

function cadastrar() {
  let nomeCriado = document.getElementById("novo-nome").value;
  let senhaCriada = document.getElementById("nova-senha").value;

  localStorage.setItem("nomeSalvo", nomeCriado);
  localStorage.setItem("senhaSalva", senhaCriada);

  alert("Conta criada! Volte para o login.");
  mostrarLogin();
}