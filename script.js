function repondre() {
  let question = document.getElementById("question").value;
  let reponse = document.getElementById("reponse");

  if (question.trim() === "") {
    reponse.innerHTML = "Pose une question d'abord.";
    return;
  }

  reponse.innerHTML = "Senghor IA réfléchit...";

  setTimeout(() => {
    reponse.innerHTML =
      "Tu as demandé : " + question + "<br><br>" +
      "Je suis Senghor IA. Je vais bientôt être connecté à une vraie intelligence artificielle.";
  }, 1000);
}
