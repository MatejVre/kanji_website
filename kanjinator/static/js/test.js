function mouseOver(id, meaning){
    document.getElementById(id).classList.add("overwrite");
    document.getElementById(id).innerHTML = meaning;
    console.log("dela");
}

function mouseOut(id, symbol){
    document.getElementById(id).classList.remove("overwrite");
    document.getElementById(id).classList.add("display_kanji");
    document.getElementById(id).innerHTML = symbol;
    console.log("dela"); 
}