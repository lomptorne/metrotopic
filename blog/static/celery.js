function deactivate(progressBarElement, progressBarMessageElement, progress){
    document.getElementById("dlbtn").disabled = true;
    progressBarElement.style.backgroundColor = '#68a9ef';
    progressBarElement.style.width = progress.percent + "%";
    var description = progress.description || "";
    progressBarMessageElement.innerHTML = progress.current + ' of ' + progress.total + ' processed. ' + description;

  };
function reactivate(){
    document.getElementById("dlbtn").disabled = false;
    document.getElementById("dlinstbtn").disabled = false;
    link =  "/media/" + document.getElementById('id_Hashtag').value + ".zip";
    document.getElementById("dlinstbtn").onclick = function () {
      location.href = String(link);
  };
  };
