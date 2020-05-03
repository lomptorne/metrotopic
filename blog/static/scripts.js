window.addEventListener("DOMContentLoaded", () => {

    //Scrollbar function
$(window).scroll(function(){
  var wintop = $(window).scrollTop(), docheight =

    $(document).height(), winheight = $(window).height();
    var scrolled = (wintop/(docheight-winheight))*100;

    $('.scroll-line').css('width', (scrolled + '%'));
});

window.onscroll = function() {scrollFunction()};



if (window.innerWidth > 1000) {
function scrollFunction() {

document.getElementById("mainbloc").style.overflowAnchor= "none"

  if (document.body.scrollTop > 95 || document.documentElement.scrollTop > 95) {
    $("#titlea").fadeIn(500);
    $("#titleb").fadeOut(0);$
    document.getElementById("articlec").style.marginLeft = "27%"


  }
  else {
    $("#titleb").fadeIn(500);
    $("#titlea").fadeOut(0);
    document.getElementById("articlec").style.width = "70%"
    document.getElementById("articlec").style.marginLeft = "auto"


  }



}
}

if (window.innerWidth < 1000) {
  document.getElementById("articlec").style.width = "95%"
}
});
