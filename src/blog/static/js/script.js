function openNav() {
  document.getElementById("overlay-nav").style.width = "100%";
}
  
function closeNav() {
  document.getElementById("overlay-nav").style.width = "0%";
}


/*archive page*/
var cards = document.querySelectorAll(".archive-card-inside"), i;

function cardOut() {
    var contents = document.querySelectorAll(".archive-card-info-contents");
    for (var i=0; i<contents.length; i++) {
        contents[i].style.opacity = 0;
    }
}

function cardIn() {
    var contents = document.querySelectorAll(".archive-card-info-contents");
    for (var i=0; i<contents.length; i++) {
        contents[i].style.opacity = 1;
    }
}

for (var i=0; i < cards.length; ++i) {
    cards[i].addEventListener('mouseout', cardOut);
    cards[i].addEventListener('mouseover', cardIn);
}
/* end archive page */

/*progress bar*/
// When the user scrolls the page, execute myFunction 
// var container = document.getElementById("progress-container");
// var sticky = container.offsetTop;

// window.onscroll = function() {progressBar()};

// var progressContainer = container.getBoundingClientRect();
//     return (
//         rect.top >= 0 &&
//         rect.left >= 0 &&
//         rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && /*or $(window).height() */
//         rect.right <= (window.innerWidth || document.documentElement.clientWidth) /*or $(window).width() */
//     );

// function progressBar() {
//   var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
//   var header = document.getElementById("detail-header");
//   var headerHeight = header.scrollHeight;
//   var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
//   var scrolled = ((winScroll - headerHeight) / (height - headerHeight)) * 100;
//   document.getElementById("progress-bar").style.width = scrolled + "%";

//   if (window.pageYOffset > sticky) {
//     container.classList.add("sticky");
//     document.getElementById("progress-bar").style.display = "block";
//   } else {
//     container.classList.remove("sticky");
//     document.getElementById("progress-bar").style.display = "none";
//   }
// }