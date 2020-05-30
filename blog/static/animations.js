
// Fade out
function fadeOutFunction(element, opacity) 
{ 
  element.style.opacity = window.getComputedStyle(element).opacity - opacity;
  var end = window.getComputedStyle(element).opacity 
  
  if ( end == 0)
  {
    clearInterval(myFunction);
    element.style.display = "none"
  }
  
}
function fadeOut(element, opacity)
{
  element = document.getElementById(element)
  myFunction = setInterval(function(){fadeOutFunction(element, opacity)}, 17)
}

// Fade in
function fadeInFunction(element, opacity) 
{ 
  element.style.opacity = window.getComputedStyle(element).opacity - opacity;
  var end = window.getComputedStyle(element).opacity 
  
  if ( end == 1)
  {
    clearInterval(myFunction);
  }
}
function fadeIn(element, opacity)
{
  element = document.getElementById(element)
  element.style.display = "inline"
  myFunction = setInterval(function(){fadeInFunction(element, -opacity)}, 17)
}

// Move horizontal
function moveHFunction(element, distance, max)
{
  element.style.transform  += "translateX(" + (distance) + "%)"

  moveCount += distance

  if (moveCount == max)
  {
    clearInterval(myFunction);
  }
}
function moveH(element, distance, max)
{
  element = document.getElementById(element)
  moveCount = 0 
  myFunction = setInterval(function(){moveHFunction(element, distance, max)}, 17);
}

// Move vertical
function moveVFunction(element, distance, max)
{
  element.style.transform  += "translateY(" + (distance) + "%)"

  moveCount += distance

  if (moveCount == max)
  {
    clearInterval(myFunction);
  }
}
function moveV(element, distance, max)
{
  element = document.getElementById(element)
  moveCount = 0 
  myFunction = setInterval(function(){moveVFunction(element, distance, max)}, 17);
}

//Rotate
function rotateFunction(element, speed, degree)
{
  element.style.transform  += "rotate(" + (speed) + "deg)"
  moveCount += speed
  
  if (moveCount == degree)
  {
    clearInterval(myFunction);
  }
}
function rotate(element, speed, degree)
{
  element = document.getElementById(element)
  moveCount = 0 
  myFunction = setInterval(function(){rotateFunction(element, speed, degree)}, 17);
}





