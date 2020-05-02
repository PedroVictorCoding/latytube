function waveInit() {
    var ocean = document.getElementById("ocean"),
    waveWidth = 10,
    waveCount = Math.floor((window.innerWidth - 5)/waveWidth),
    docFrag = document.createDocumentFragment();

    for(var i = 0; i < waveCount; i++){
    var wave = document.createElement("div");
    wave.className += " wave";
    docFrag.appendChild(wave);
    wave.style.webkitAnimationDelay = (i/100) + "s";
    wave.style.left = i * waveWidth + "px";
    }

    ocean.appendChild(docFrag);
}
