
var images = ['../images/g1.jpg', '../images/g2.jpg', '../images/g3.jpg', '../images/g4.jpg', '../images/g5.jpg', '../images/g6.jpg',
                '../images/g7.jpg', '../images/g8.jpg']

let body = document.getElementById("body")

var i = 0;
setInterval(function() {
      body.style.backgroundImage = 'url(' + images[i] + ')';
      body.style.transition = "all 3s";
      i = i + 1;
      if (i == images.length) {
        i =  0;
      }
}, 3000);