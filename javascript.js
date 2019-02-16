

// function opensubmenu() {
//   document.getElementById("opener").addEventListener("click", () => {
//     if (document.getElementsByClassName("submenu-1")[0].style.display == "block")
//       document.getElementsByClassName("submenu-1")[0].style.display = "none";
//     else
//       document.getElementsByClassName("submenu-1")[0].style.display = "block";
//   });

//   document.getElementById("opener-2").addEventListener("click", () => {
//     if (document.getElementsByClassName("submenu-2")[0].style.display == "block")
//       document.getElementsByClassName("submenu-2")[0].style.display = "none";
//     else
//       document.getElementsByClassName("submenu-2")[0].style.display = "block";
//   });
// }
// opensubmenu();

// When the user scrolls down 20px from the top of the document, slide down the navbar
// window.onscroll = function () { scrollFunction() };

// function scrollFunction() {
//   let elements = document.getElementsByClassName("product-card");
//   document.getElementById("temporary").innerHTML = document.body.scrollTop;
//   if ((document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) && (document.body.scrollTop < 270 || document.documentElement.scrollTop < 270)) {
//     // for (var index = 0; index <= 3; index++) {
//     //  var element = elements[index];
//     document.getElementById("product-showcase").style.right = "0";
//     //  element.style.top="0";    
//     //  console.log(element);
//   }
//   else {
//     document.getElementById("product-showcase").style.right = "-1050px";
//   }
// }

var isScrolling = false;
window.addEventListener("scroll", throttleScroll, false);

function throttleScroll(e) {
  if (isScrolling == false) {
    window.requestAnimationFrame(function () {
      scrolling(e);
      isScrolling = false;
    });
  }
  isScrolling = true;
}

document.addEventListener("DOMContentLoaded", scrolling, false);

var listItems = document.querySelectorAll("#product-showcase div");
// var firstBox = document.querySelector("#firstBox");
// var secondBox = document.querySelector("#secondBox");

function scrolling(e) {

  // if (isPartiallyVisible(firstBox)) {
  //   firstBox.classList.add("active");
  //   document.body.classList.add("colorOne");
  //   document.body.classList.remove("colorTwo");
  // } else {
  //   document.body.classList.remove("colorOne");
  //   document.body.classList.remove("colorTwo");
  // }

  // if (isFullyVisible(secondBox)) {
  //   secondBox.classList.add("active");

  //   document.body.classList.add("colorTwo");
  //   document.body.classList.remove("colorOne");
  // }

  for (var i = 0; i < (listItems.length); i++) {
       var listItem = listItems[i];
      //  for (var index = 0; index < array.length; index++) {
      //    var element = array[index];
         
      //  }
    if (isPartiallyVisible(listItem)) {
      listItem.classList.add("active");
    } else {
      listItem.classList.remove("active");
    }
  }
}

function isPartiallyVisible(el) {
  var elementBoundary = el.getBoundingClientRect();

  var top = elementBoundary.top;
  var bottom = elementBoundary.bottom;
  var height = elementBoundary.height;

  return ((top + height >= 60) && (200 + window.innerHeight >= bottom));
}

function isFullyVisible(el) {
  var elementBoundary = el.getBoundingClientRect();

  var top = elementBoundary.top;
  var bottom = elementBoundary.bottom;

  return ((top >= 0) && (bottom <= window.innerHeight));
}
