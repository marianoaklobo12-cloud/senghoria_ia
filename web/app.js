const bouton =
document.querySelector(".create");


bouton.onclick=function(){

let texte =
document.querySelector("#prompt").value;


if(texte===""){

alert("Décris ta vidéo");

return;

}


alert(
"Senghor IA prépare ta vidéo :\n\n"
+ texte
);


};
