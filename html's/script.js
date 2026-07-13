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