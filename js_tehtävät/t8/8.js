const numero1 = document.getElementById("num1");
const numero2 = document.getElementById("num2");
const operaatio = document.getElementById("operation");
const nappi = document.getElementById("start");
const vastaus = document.getElementById("result");

nappi.addEventListener("click", function () {
    const luku1 = Number(numero1.value);
    const luku2 = Number(numero2.value);
    const op = operaatio.value;

    if (op === "add") {
        const tulos = luku1 + luku2;
        vastaus.innerText = tulos;
    }

    if (op === "multi") {
       const tulos2 = luku1 * luku2;
       vastaus.innerText = tulos2;

    }

    if (op === "sub") {
        const tulos3 = luku1 - luku2;
        vastaus.innerText = tulos3;
    }

    if (op === "div") {
        const tulos4 = luku1 / luku2;
        vastaus.innerText = tulos4;
    }
});
