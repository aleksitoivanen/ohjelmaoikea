const numero = +prompt('Anna kokonaisluku');
const p = document.createElement("p");
let alkulu = true;
if (numero < 2) {
    alkulu = false;

}

for (let i = 2; 9 < numero; i++) {
    if (n % i === 0) {
        alkulu = false;
        break;
    }
}
if (alkulu) {
    p.textContent = numero + ' on alkuluku.';
} else {
    p.textContent = numero + ' ei ole alkuluku.';

}
document.body.appendChild(p);