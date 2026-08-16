let choix = {};


document.querySelectorAll(".choix").forEach(bouton=>{


bouton.onclick=function(){


let type=this.dataset.type;

let valeur=this.dataset.value;


choix[type]=valeur;


localStorage.setItem(
"SenghorParametres",
JSON.stringify(choix)
);


this.style.background="#00eaff";


};


});





document.querySelector("#videos").onchange=function(){


let liste=document.querySelector("#listeVideos");

liste.innerHTML="";


for(let video of this.files){

let p=document.createElement("p");

p.innerHTML="🎬 "+video.name;

liste.appendChild(p);

}


};





document.querySelector("#assembler").onclick=function(){


alert(
"Préparation assemblage de "+
document.querySelector("#videos").files.length+
" vidéos"
);


localStorage.setItem(
"assemblage",
"demande"
);


};





document.querySelector("#termine").onclick=function(){


localStorage.setItem(
"SenghorParametres",
JSON.stringify(choix)
);


document.querySelector("#message").innerHTML=
"✅ Terminé";


setTimeout(()=>{

window.location.href="index.html";

},1000);


};
