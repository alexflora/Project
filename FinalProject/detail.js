


function getProductDetail() {

    $.get('https://5d76bf96515d1a0014085cf9.mockapi.io/product/'+window.location.search.substring(1), function (productDetail) {
        
        $("#h1").text(productDetail.name)
        $("#h2").text(productDetail.brand)
        $("#price").text(productDetail.price)
        $("#des").text(productDetail.description)
        photo0 = productDetail.photos[0];
        photo1 = productDetail.photos[1];
        photo2 = productDetail.photos[2];
        photo3 = productDetail.photos[3];
        photo4 = productDetail.photos[4];
        photo5 = productDetail.photos[5];

        createProductPage(
            photo0,
            photo1,
            photo2,
            photo3,
            photo4,
            photo5
        );
    });
 
}
getProductDetail();

function createProductPage(
img0,
img1,
img2,
img3,
img4
) {

// Product Preview Image Main
var photo0 = document.getElementById("productImg");
photo0.src = img0;

// Product Preview Image 0
var photo0 = document.getElementById("img0");
photo0.src = img0;

// Product Preview Image 1
var photo1 = document.getElementById("img1");
photo1.src = img1;

// Product Preview Image 2
var photo2 = document.getElementById("img2");
photo2.src = img2;

    // Product Preview Image 3
    if (photo3 != undefined) {
        var photo3 = document.getElementById("img3");
        photo3.src = img3;       
    }
    // Product Preview Image 4

if (photo4 != undefined) {
    var photo4 = document.getElementById("img4");
    photo4.src = img4;       
}

// ---------------- Change Preview Image OnClick -------
function changeImage() {
  // Photo 0
  photo0.addEventListener("click", function() {
    productImg.src = img0;
    Sibling("img0"); 
  });

  // Photo 1
  photo1.addEventListener("click", function() {
    productImg.src = img1;
    Sibling("img1"); 
  });
  // Photo 2
  photo2.addEventListener("click", function() {
    productImg.src = img2;
    Sibling("img2"); 
  });

  // Photo 3
  photo3 ?.addEventListener("click", function() {
    productImg.src = img3;
    Sibling("img3"); 
  });

  // Photo 4
  photo4 ?.addEventListener("click", function() {
    productImg.src = img4;
    Sibling("img4"); 
  });

  function Sibling(id) {
    var divs = document.querySelectorAll('.previewImg img'); 
    for (i = 0; i < divs.length; i++)
    {
      if (divs[i].id == id) {
        document.getElementById(divs[i].id).classList.add("active")
      }
      else {
        document.getElementById(divs[i].id).classList.remove("active")
      }
}
    
  }
}
changeImage();
}
// function addcart(){
//   //window.location.href = "file:///D:/assingment%20edyoda/Javascript/FinalProject/order.html?" + window.location.search.substring(1)
// }


var currentObj = null;
$.get('https://5d76bf96515d1a0014085cf9.mockapi.io/product/' + window.location.search.substring(1), function(data, status) {
        currentObj = data;
    })
$("#btn-add-to-cart").click(function() {
        
        var productList = window.localStorage.getItem('product-list');
        productList = productList === null || productList === '' ? [] : productList;
        productList = productList.length > 0 ? JSON.parse(productList) : [];

        // productList.push(currentObj);
        // window.localStorage.setItem('product-list', JSON.stringify(productList));
        console.log("Productlist",productList);

        var foundAtPos = -1;
        for(var i=0; i < productList.length; i++) {
            // console.log(productList[i].id);
            if(parseInt(productList[i].id) == parseInt(currentObj.id)) {
                foundAtPos = i;
            }
        }

        if(foundAtPos > -1) {
            productList[foundAtPos].count = productList[foundAtPos].count + 1;
            console.log("-1 pos",productList[foundAtPos].count);
            window.localStorage.setItem('product-list', JSON.stringify(productList));
        } else {
            currentObj.count = 1;
            productList.push(currentObj);
            console.log("0 position",productList);
            window.localStorage.setItem('product-list', JSON.stringify(productList));
        }

        var totalCount = 0;
        for(var i=0; i<productList.length; i++) {
            totalCount = totalCount + productList[i].count;
        }
    
        $('#cart-count').html(totalCount);
    })

