//btn add to cart animation
$(".js-cart-buttons").click(function () {
var id  = "#"+ $(this).attr('id');
console.log(id);
$(id).addClass("btn-animate");
});


$(function(){
	PhotosWidth();
	ArrangementCartIcons();//calling function on window load
	$(window).resize(function(){
		PhotosWidth();
		ArrangementCartIcons();//calling function on window resize
	});
});
