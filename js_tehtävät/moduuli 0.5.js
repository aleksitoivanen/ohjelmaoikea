const vuosi = +prompt('Anna vuosi');
const tulos = document.createElement("p");

if (vuosi % 400 === 0) {
    tulos.textContent = vuosi + ' on karkausvuosi.';
} else if (vuosi % 100 === 0) {
    tulos.textContent = vuosi + ' ei ole karkausvuosi.';
} else if (vuosi % 4 === 0) {
   tulos.textContent = vuosi + ' on karkausvuosi';
} else {
    tulos.textContent = vuosi + 'ei ole karkausvuosi';
}

document.body.appendChild(tulos);
