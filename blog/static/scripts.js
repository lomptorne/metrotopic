
function caca()
{

navTools = document.getElementById("navTools")
navTools.style.visibility = 'visible'

var tl = anime.timeline({
  
});

tl
.add({
  targets: '#navBtn',
  translateX: -navTools.offsetWidth - 10 ,
  rotate: 180,
  visibility: 'hidden',
  easing: 'easeInOutExpo'

})
.add({
  
  targets: '#navTools',
  opacity: 1,
  easing: 'easeInOutExpo'

});


}





window.addEventListener("DOMContentLoaded", () => {

//Scrollbar function
$(window).scroll(function()
{
  var wintop = $(window).scrollTop(), docheight =

  $(document).height(), winheight = $(window).height();
  var scrolled = (wintop/(docheight-winheight))*100;

  $('.scroll-line').css('width', (scrolled + '%'));
}
);



// load only on article page 
var elementExists = document.getElementById("articlec");
if (typeof(elementExists) != 'undefined' && elementExists != null)
{
  document.body.style.backgroundImage = "none";
}

// Post page modulation function
if (window.innerWidth > 1000) 
{
  // load only on article page 
  var elementExists = document.getElementById("articlec");
  if (typeof(elementExists) != 'undefined' && elementExists != null)
  {
    window.onscroll = function() {scrollFunction()};
  }

  function scrollFunction() 
  {

    document.getElementById("flow").style.overflowX= "visible"

    if (document.body.scrollTop > 95 || document.documentElement.scrollTop > 95) 
    {
      $("#titlea").fadeIn(500);
      $("#titleb").fadeOut(0);$
      document.getElementById("articlec").style.marginLeft = "28%"
    }
    else 
    {
      $("#titleb").fadeIn(500);
      $("#titlea").fadeOut(0);
      document.getElementById("articlec").style.width = "70%"
      document.getElementById("articlec").style.marginLeft = "auto"
    }
  }
}

// If smallscreen
if (window.innerWidth < 1000) 
{
  var elementExists = document.getElementById("articlec");

  if (typeof(elementExists) != 'undefined' && elementExists != null)
  {
    document.getElementById("articlec").style.width = "95%"
  }
}

// Rich text editor for the add page 
tinymce.init(
{
  selector: '#editor',
  toolbar: 'undo redo | bold italic underline | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | image | restoredraft ',
  height : "480",
  resize: false,
  plugins: "image imagetools autosave"
}
);

}
);
