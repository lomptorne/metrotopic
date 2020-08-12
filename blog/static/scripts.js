// refresh motivateur
function validateOFrm(){

  var x, text;

  // Get the value of the input field with id="numb"
  x = document.getElementById("imgNbr").value;

  // If x is Not a Number or less than one or greater than 10
  if (isNaN(x) || x < 1 || x > 10) {
    alert("Name must be filled out");
  } else {
    text = "Input OK";
  }
  document.getElementById("demo").innerHTML = text;


}
// Sidebar for mobile
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
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

// Determine padding-top depending on the navbar size
var navHeight = document.getElementById("nav").clientHeight;
document.getElementById("mainblock").style.paddingTop = navHeight + "px"


// load only on article page 
var elementExists = document.getElementById("articlec");
if (typeof(elementExists) != 'undefined' && elementExists != null)
{
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
    document.getElementById("viewPanel").style.visibility = "visible"
    document.getElementById("mySidenav").style.paddingTop = navHeight + "px"
  }
}



// Rich text editor for the add page 
tinymce.init(
{
  selector: '#editor',
  toolbar: 'undo redo | bold italic underline | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | image | restoredraft ',
  height : "480",
  resize: false,
  plugins: "image imagetools autosave",
  image_caption: true,
  
}
);





}
);
