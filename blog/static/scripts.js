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

// If smallscreen
if (window.innerWidth < 1000) {
  document.getElementById("articlec").style.width = "95%"
}

tinymce.init({
  selector: '#editor',
  toolbar: 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment',
  height : "480",
  resize: false
});


});
