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

$(document).ready(function() {


  $( "#dlbtn" ).click(function() {

event.preventDefault();
var hashtag = document.getElementById("id_Hashtag").value;
var imgNbr = parseInt(document.getElementById("id_Image_numbers").value);
let url = `https://www.instagram.com/explore/tags/${hashtag}/?__a=1`;
var mydata;
var urlList = [];
var infinite;
document.getElementById("dlbtn").disabled = true;
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });
  setTimeout(function() {
  $.ajax({
  url: url,
  async: false,
  dataType: 'json',
  success: function (json) {
    
    mydata = json

    }
  });



  jsonDump = mydata.graphql.hashtag.edge_hashtag_to_media
  

  for (var i = 0; i < jsonDump.edges.length; i++) { 
    urlList.push(jsonDump.edges[i].node.display_url);
}
 var urlLength = urlList.length

 if(urlLength >= 50)
 {
   while(urlLength < imgNbr ){
 
 
     var urlNext = url + "&max_id=" + mydata.graphql.hashtag.edge_hashtag_to_media.page_info.end_cursor
 
     $.ajax({
       url: urlNext,
       async: false,
       dataType: 'json',
       success: function (json) {
         
         mydata = json
     
         }
       });
 
     jsonDump = mydata.graphql.hashtag.edge_hashtag_to_media
     for (var i = 0; i < jsonDump.edges.length; i++) { 
       urlList.push(jsonDump.edges[i].node.display_url);
     }
     urlLength = urlList.length
     infinite ++;
     if (infinite === 10) { break; }
   }
 
 }
 
 
 if (urlLength > imgNbr) {
     accuration = urlLength- imgNbr
     for (var i = 0; i < accuration; i++) { 
       urlList.pop()
     }
 }
 
 console.log(urlList)
   $.ajax(
     {
         'url': "/instascrap",
         'type': 'POST',
         'contentType': 'application/json; charset=UTF-8',
         'data': JSON.stringify({'updated_data':urlList}),
         'dataType': 'text',
         'success': function ( return_data ) {
             
                             //success body
             
                           }
   });
 




}, 10);










  
  
  

});

});