

const name = prompt('Type your name.');
const greeting = `Hello ${name}`;
const teksti = document.createElement('p');
teksti.innerHTML = greeting;
document.body.appendChild(teksti);