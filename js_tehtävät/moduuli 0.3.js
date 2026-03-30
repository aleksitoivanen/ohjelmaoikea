const numero = +prompt('Anna kokonaisluku');
const numero2 = +prompt('Anna toinen kokonaisluku');
const numero3 = +prompt('Anna kolmas kokonaisluku');

const summa = numero + numero2 + numero3;
const tulo = numero * numero2 * numero3;
const keskiarvo = summa / 3;

const teksti = document.createElement("p");
teksti.innerHTML = "Antamiesi lukujen summa on " + summa + "<br>Antamiesi lukujen tulo on " + tulo + "<br>Antamiesi lukujen keskiarvo on " + keskiarvo;

document.body.appendChild(teksti);