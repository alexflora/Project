

function CheckOut() {
    var productList = window.localStorage.getItem('product-list');
    console.log(productList)
    var item = $('.itemdiv').empty();
    var over = $('overall').empty();
    // Iterate through the card data and render cards
    for (var i = 0; i < productList.length; i++) {
        var card = productList[i];
        // Create a new card element
        var cardElement = $('<div class="imgdivs">');
        var imgElement = $('<img class="img">').attr('src', card.preview);
        var disdiv = $('<div class="discription">');
        var h3Element = $('<h3 id="h3">').text(card.head);
        var priceElement = $('<p id="price">').text(card.price);

        // Append the card elements to the container
        cardElement.append(imgElement);
        disdiv.append(h3Element);
        disdiv.append(priceElement);
        item.append(cardElement);
        item.append(disdiv);
        over.append(item)

    }
}
