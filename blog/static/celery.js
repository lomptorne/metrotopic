function deactivate(progressBarElement, progressBarMessageElement, progress){
    document.getElementById("dlbtn").disabled = true;
    progressBarElement.style.backgroundColor = '#68a9ef';
    progressBarElement.style.width = progress.percent + "%";
    var description = progress.description || "";
    progressBarMessageElement.innerHTML = description + progress.current + ' / ' + progress.total ;

  };
function reactivate(resultElement, result){
    document.getElementById("dlbtn").disabled = false;
    $("#dlinstbtn").removeClass("btn btn-secondary btn-lg").addClass("btn btn-success btn-lg")
    document.getElementById("dlinstbtn").disabled = false;
    link =  "/media/" + String(result);
    document.getElementById("dlinstbtn").onclick = function () {
      location.href = String(link);
  };
  };
  function errorHandler(progressBarElement, progressBarMessageElement, excMessage) {
    progressBarElement.style.backgroundColor = '#dc4f63';
    progressBarMessageElement.innerHTML = "Error : " + excMessage;
};

