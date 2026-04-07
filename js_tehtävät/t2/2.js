const target = document.getElementById("target");
const li1 = document.createElement("li1");
li1.innerText = "first item";

const li2 = document.createElement("li");
li2.innerText = "second item";
li2.classList.add("my-item");

const li3 = document.createElement("li");
li3.innerText = "Third item";

target.appendChild(li1);
target.appendChild(li2);
target.appendChild(li3);
