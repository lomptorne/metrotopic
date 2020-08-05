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


function dumper(){
  
  let url = "https://www.instagram.com/explore/tags/shibainu/?__a=1";


  var mydata = [];
  $.ajax({
    url: url,
    async: false,
    dataType: 'json',
    success: function (json) {
      mydata = json;
    }
  });
  dump = mydata.graphql.hashtag.edge_hashtag_to_media.edges
console.log(dump)
}


