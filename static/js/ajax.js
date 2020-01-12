function addOrUpdateUrlParam(name, value)
{
  var href = window.location.href;
  var regex = new RegExp("[&\\?]" + name + "=");
  if(regex.test(href))
  {
    regex = new RegExp("([&\\?])" + name + "=\\w+");
    window.location.href = href.replace(regex, "$1" + name + "=" + value);
  }
  else
  {
    if(href.indexOf("?") > -1)
      window.location.href = href + "&" + name + "=" + value;
    else
      window.location.href = href + "?" + name + "=" + value;
  }
}

// $(function() {
//     let images = document.querySelectorAll(".lazyload");
//     let images2 = document.querySelectorAll(".card-img-top");
//     lazyload(images);
//     lazyload(images2);
//   });
  
$(document).ready(function () {
    var lazyLoadInstance = new LazyLoad();
});

$(function() {

    var $allVideos = $("iframe[src^='https://www.youtube.com']"),
    $fluidEl = $("figure");

	$allVideos.each(function() {

	  $(this)
	    // jQuery .data does not work on object/embed elements
	    .attr('data-aspectRatio', this.height / this.width)
	    .removeAttr('height')
	    .removeAttr('width');

	});

	$(window).resize(function() {

	  var newWidth = $fluidEl.width();
	  $allVideos.each(function() {

	    var $el = $(this);
	    $el
	        .width(newWidth)
	        .height(newWidth * $el.attr('data-aspectRatio'));

	  });

	}).resize();

});
  
// $(document).ready(function () {
//   $('#random_sort').on('click', function random () {
//       $.ajax({
//           type: 'GET',
//           url: '/filter',
//           datatype: 'JSON',
//           data: {
//             url: window.location.href
//           },
//           success: function (data) {
//               $('#placeholder').html("")
//               $('#placeholder').append(data)
//           }
//       })
//   });
// });
