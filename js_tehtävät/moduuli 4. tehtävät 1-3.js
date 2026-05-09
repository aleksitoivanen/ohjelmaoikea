const lomake = document.querySelector('#searchForm');
const hakukentta = document.querySelector('#query');
const tulokset = document.querySelector('#results');

lomake.addEventListener('submit', async (tapahtuma) => {
    tapahtuma.preventDefault();

    const hakusana = hakukentta.value;
    const vastaus = await fetch(`https://api.tvmaze.com/search/shows?q=${hakusana}`);
    const sarjat = await vastaus.json();

    console.log(sarjat);
    tulokset.innerHTML = '';
    for (const sarja of sarjat) {
    const artikkeli = document.createElement('article');

    const nimi = document.createElement('h2');
    nimi.textContent = sarja.show.name;

    const linkki = document.createElement('a');
    linkki.href = sarja.show.url;
    linkki.textContent = 'Linkki sarjan tietoihin';
    linkki.target = '_blank';

    const kuva = document.createElement('img');
    kuva.src = sarja.show.image?.medium || '';
    kuva.alt = sarja.show.name;

    const kuvaus = document.createElement('div');
    kuvaus.innerHTML = sarja.show.summary || 'Ei kuvausta saatavilla.';

    artikkeli.appendChild(nimi);
    artikkeli.appendChild(linkki);
    artikkeli.appendChild(document.createElement('br'));

    if (sarja.show.image?.medium) {
      artikkeli.appendChild(kuva);
    }

    artikkeli.appendChild(kuvaus);
    tulokset.appendChild(artikkeli);
  }
});