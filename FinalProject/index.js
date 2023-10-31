$.get('https://5d76bf96515d1a0014085cf9.mockapi.io/product/', function (productList) {
        
var mainSection = document.getElementById("coths-ass-section");
// Heading section
var heading = document.createElement("h2");
heading.innerHTML = "Clothing for Men and Women";
heading.className = "headstyle";
mainSection.appendChild(heading);

// Clothing section
var clothingparent = document.createElement("div");
clothingparent.className = "clothparent";
var clothingsection = document.createElement("div");
clothingsection.className = "clothdiv";

        for (var i = 0; i < productList.length; i++){
            if (productList[i].isAccessory === false) {
                // cothcard
                var clothcard = document.createElement("div");
                clothcard.className = "cothcard";
        
                var clothanchor = document.createElement("a");
                clothanchor.className = "clothahstyle";
                clothanchor.href = "\detail.html?"+productList[i].id
                clothcard.appendChild(clothanchor);
        
                var imgDiv = document.createElement("div");
                imgDiv.className = "imgdiv";
                
                var modelImage = document.createElement("img");
                modelImage.className = "model-image";
                modelImage.src = productList[i].preview;
        
                var detailsdiv = document.createElement("div");
                detailsdiv.className = "detailstyle";
        
                var cardhead = document.createElement("div");
                cardhead.className = "cardheadstyle";
                cardhead.innerHTML = productList[i].name;
        
                var cardbrand = document.createElement("div");
                cardbrand.className = "cardbrandstyle";
                cardbrand.innerHTML = productList[i].brand;
        
                var cardprice = document.createElement("div");
                cardprice.className = "cardpricestyle";
                cardprice.innerHTML = productList[i].price;
        
                imgDiv.appendChild(modelImage);
                detailsdiv.appendChild(cardhead);
                detailsdiv.appendChild(cardbrand);
                detailsdiv.appendChild(cardprice);
        
                clothanchor.appendChild(imgDiv);
                clothanchor.appendChild(detailsdiv);
        
                clothingsection.appendChild(clothcard)
        
            }
    }
    clothingparent.appendChild(clothingsection);
    mainSection.appendChild(clothingparent);
    

    var heading = document.createElement("h2");
  heading.innerHTML = "Accessories for Men and Women";
  heading.className = "headstyle";
  mainSection.appendChild(heading);

  // Clothing section
  var clothingparent = document.createElement("div");
  clothingparent.className = "clothparent";
  var clothingsection = document.createElement("div");
  clothingsection.className = "clothdiv";

  for (var i = 0; i < productList.length; i++){
    if (productList[i].isAccessory === true) {
        // cothcard
        var clothcard = document.createElement("div");
        clothcard.className = "cothcard";

        var clothanchor = document.createElement("a");
        clothanchor.className = "clothahstyle";
        clothanchor.href = "\detail.html?"+productList[i].id
        clothcard.appendChild(clothanchor);

        var imgDiv = document.createElement("div");
        imgDiv.className = "imgdiv";
        
        var modelImage = document.createElement("img");
        modelImage.className = "model-image";
        modelImage.src = productList[i].preview;

        var detailsdiv = document.createElement("div");
        detailsdiv.className = "detailstyle";

        var cardhead = document.createElement("div");
        cardhead.className = "cardheadstyle";
        cardhead.innerHTML = productList[i].name;

        var cardbrand = document.createElement("div");
        cardbrand.className = "cardbrandstyle";
        cardbrand.innerHTML = productList[i].brand;

        var cardprice = document.createElement("div");
        cardprice.className = "cardpricestyle";
        cardprice.innerHTML = productList[i].price;

        imgDiv.appendChild(modelImage);
        detailsdiv.appendChild(cardhead);
        detailsdiv.appendChild(cardbrand);
        detailsdiv.appendChild(cardprice);

        clothanchor.appendChild(imgDiv);
        clothanchor.appendChild(detailsdiv);

        clothingsection.appendChild(clothcard)

    }
  }
  clothingparent.appendChild(clothingsection);
  mainSection.appendChild(clothingparent);
    });
  
document.onload = function () {
    var productList = window.localStorage.getItem('product-list');
  if (productList) {
    productList = JSON.parse(productList);
    var productListLength = productList.length;
    $("#cart-count").text(productListLength);
  }
}    
/*$('.slickclass').slick({
  dots: true,
  infinite: false,
  speed: 300,
  slidesToShow: 1,
  slidesToScroll: 1,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});*/
// $(document).ready(function(){
//   $('.slickclass').slick({
//   dots: true,
//   infinite: true,
//   speed: 300,
//   slidesToShow: 1,
//   slidesToScroll: 1,
//   });
// });
function CheckOut() {
  window.location.href = "file:///D:/assingment%20edyoda/Javascript/FinalProject/order.html?" + window.location.search.substring(1)
}